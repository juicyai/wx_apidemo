import logging,json
import time

from requests.structures import CaseInsensitiveDict
import requests
from utils.handleJson import ParseJson
from utils.parseYaml import ParseYaml
from wx_api.sessionAndToken import SessionAndToken

#session=requests.session()

class BaseApi:
    log: logging.Logger
    token:str
    def __init__(self):
        # self.log=self.get_logger()
        self.session=self._session()
        #self._session=session
        self._token=self.get_token()
        self.url="https://www.baidu.com",
    #
    # @classmethod
    # def get_logger(cls,level=logging.DEBUG):
    #     cls.log=logging.getLogger("wx_api")
        # return cls.log
    # @classmethod
    # def get_session(cls):
    #     return IniSession
    @classmethod
    def _session(cls):
        # IniSession.session
        return SessionAndToken.session
    @classmethod
    def get_token(cls):
        return SessionAndToken._token
    @classmethod
    def get_uid(cls):
        uid=str(time.time()).replace('.','')
        return uid[:12]

    @classmethod
    def get_template(cls,filename,dict)->dict:
        """
        模板方法，用于替换json body中的字段
        :param filename: 存储模板的文件名，不需要填写后缀名
        :param dict: 传入需要替换的字段
        :return: 使用eval方法将str转换成dict返回
        """
        js=ParseJson.readJson(filename)
        tmp=ParseJson.parsejson(str(js),dict)
        # cls.get_logger().debug(tmp)
        return eval(str(tmp))

    method,url,params,json,data="","",None,None,None

    def source(self,filename,meth):
        self.data_all = ParseYaml.readYaml(filename)  # 读取yaml文件
        print("data_all:::",self.data_all)
        #self.data_ls = self.data_all[meth]  # 取出对应的meth参数列表
        if meth in self.data_all:
            self.data_ls = self.data_all[meth][0] #todo:联调时需要改进
            print("data_ls:::", self.data_ls)
        self.method=str(self.data_ls["method"]).lower() #必选参数
        self.url=self.data_ls["url"] #必选参数
        return self
    def set_params(self,**kwargs):
            if "params" in self.data_ls:
                self.params=self.data_ls["params"]
                for sub in self.params:
                    if sub=="access_token":
                        self.params[sub]=self._token
                    elif sub in kwargs:
                        self.params[sub]=kwargs[sub]

                print("param:::",self.params)
            return self

    def set_json(self,json_data):
        self.json=json_data
        return self


    def run(self):
            self.response=self.session.request(self.method,self.url,
                                               params=self.params,
                                               json=self.json,data=self.data)
            return self

    def validate(self,key:str,expected_value):
        r_:requests.Response=self.response #记录当前的key
        keys=key.split(".") #取出待比较的value， eg:status_code, header.server
        #todo:
        for k in keys:
            if isinstance(r_,requests.Response):
                r_=getattr(r_,k)
            elif isinstance(r_,CaseInsensitiveDict):
                r_=getattr(r_,k)
        assert r_ == expected_value
        return self

    def get(self,url,params=None,**kwargs):
        return requests.get(url,params=params,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return requests.post(url,data=data,json=json,**kwargs)


if __name__=="__main__":
    SessionAndToken.create_session().get_token()
    BaseApi().source("Department", "create_").set_params()



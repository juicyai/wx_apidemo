import logging,json
import time

from requests.structures import CaseInsensitiveDict
import requests
from requests_toolbelt import MultipartEncoder

from utils.handleJson import ParseJson
from utils.parseYaml import ParseYaml
from wx_api.sessionAndToken import SessionAndToken

#session=requests.session()

class BaseApi:
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    _log = logging.getLogger("wx")
    _log.setLevel(level=logging.DEBUG)
    def __init__(self):
        # logging.basicConfig(
        #                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p',
        #                     level = logging.DEBUG)
        self.session=self._session()
        #self._session=session
        self._token=self.get_token()
        # self.url="https://www.baidu.com"

    @property
    def log(self):
        return self._log

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
        cls._log.info("js template:{}".format(tmp))
        return eval(str(tmp))

    def ini_request(self): #初始化request参数
        self.method,self.url,self.params,self.json,self.data,self.headers="","",None,None,None,None

    def source(self,filename,meth):
        self.ini_request()
        self.data_all = ParseYaml.readYaml(filename)  # 读取yaml文件
        self.log.info(str("data_all:::{}".format(self.data_all)))
        #self.data_ls = self.data_all[meth]  # 取出对应的meth参数列表
        if meth in self.data_all:
            self.data_ls = self.data_all[meth][0] #todo:联调时需要改进
            self.log.info(str("data_ls:::{}".format(self.data_ls)))
        self.method=str(self.data_ls["method"]).lower() #必选参数
        self.url=self.data_ls["url"] #必选参数
        return self

    def set_headers(self,headers:dict):
        self.headers=headers
        return self
    def set_data(self,data):
        self.data=data
        return self
    def set_params(self,**kwargs): #access_token默认从yaml中读取，需传入其他关键字参数
            if "params" in self.data_ls:
                self.params={}
                for sub in self.data_ls["params"]:
                    if sub=="access_token":
                        self.params[sub]=self._token
                    elif sub in kwargs:
                        self.params[sub]=kwargs[sub]

                self.log.info("param:::",self.params)
            return self

    def set_json(self,json_data):
        self.json=json_data
        self.log.info(self.json)
        return self
    def get_multipartm(self,fields:dict)->MultipartEncoder:
        # m=MultipartEncoder(
        #     fields={'field0': 'value', 'field1': 'value',
        #             'field2': ('filename', open('file.py', 'rb'), 'text/plain')}
        # )
         m=MultipartEncoder(
            fields=fields
                )
         return m


    def run(self):
            self.response=self.session.request(self.method,self.url,
                                               params=self.params,
                                               json=self.json,data=self.data,headers=self.headers)
            return self

    def validate(self,key:str,expected_value): #校验body
        r_:requests.Response=self.response #记录当前的key
        keys=key.split(".") #取出待比较的value， eg:status_code, header.server
        #todo:
        for k in keys:
            if isinstance(r_,requests.Response):
                if k=="json()":
                    r_=r_.json()
                else:
                    r_=getattr(r_,k)
            elif isinstance(r_,(CaseInsensitiveDict,dict)):
                r_=r_[k]
            # elif isinstance(r_,list):
            #     for ls in r_:

        assert r_ == expected_value,"actual value is:{},while expected_value is {}".format(r_,expected_value)
        return self

    def get(self,url,params=None,**kwargs):
        return requests.get(url,params=params,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return requests.post(url,data=data,json=json,**kwargs)


if __name__=="__main__":
    SessionAndToken.create_session().get_token()
    BaseApi().source("Department", "create_").set_params()



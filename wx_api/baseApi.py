import logging,json
import time

import requests

from utils import parseYaml
from utils.handleJson import ParseJson
from utils.parseYaml import ParseYaml
from wx_api.getToken import GetToken
from wx_api.iniSession import IniSession

#session=requests.session()
class BaseApi:
    log: logging.Logger
    def __init__(self):
        self.log=self.get_logger()
        self.session:requests.session()=self._session()
        #self._session=session
        self._token=self.get_token()
        self.url="https://www.baidu.com",

    @classmethod
    def get_logger(cls,level=logging.DEBUG):
        cls.log=logging.getLogger("wx_api")
        return cls.log
    @classmethod
    def get_session(cls):
        return IniSession
    @classmethod
    def _session(cls):
        s=cls.get_session().session
        return s
    @classmethod
    def get_token(cls):
        return GetToken.get_token()
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
        cls.get_logger().debug(tmp)
        return eval(str(tmp))

    method,url,params,json,data="","",None,None,None
    def run(self,filename,method):
        data_yaml=ParseYaml.readYaml(filename)


        self.reponse=self.session.request(self.method,self.url,params=self.params,data=self.data,)
        #todo:

        return self

    def validate(self,key,expected_value):

        #todo:
        self.reponse.

        pass

    def get(self,url,params=None,**kwargs):
        return requests.get(url,params=params,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return requests.post(url,data=data,json=json,**kwargs)

    @classmethod
    def set_params():
        for k,v in params.items():
            if k=="access-token":






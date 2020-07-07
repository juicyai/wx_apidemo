import logging,json
import time

import requests

from utils.handleJson import ParseJson
from wx_api.getToken import GetToken


class BaseApi:
    log: logging.Logger
    def __init__(self):
        self.log=self.get_logger()
        self._token=self.get_token()

    @classmethod
    def get_logger(cls,level=logging.DEBUG):
        cls.log=logging.getLogger("wx_api")
        return cls.log

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
        :return:
        """
        js=ParseJson.readJson(filename)
        tmp=ParseJson.parsejson(str(js),dict)
        cls.get_logger().debug(tmp)
        return eval(str(tmp))


    def get(self,url,params=None,**kwargs):
        return requests.get(url,params=params,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return requests.post(url,data=data,json=json,**kwargs)
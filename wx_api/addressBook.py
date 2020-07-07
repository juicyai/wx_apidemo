import logging

import requests

from wx_api.baseApi import BaseApi


class AddressBook(BaseApi):
    logging.basicConfig(level=logging.DEBUG)
    def create_member(self,**kwargs):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params={
            "access_token": self._token
        }
        logging.debug(params)
        paylaod=self.get_template("create_body",kwargs)
        r=self.post(url,params=params,json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r
    def create_department(self,**kwargs):
        url="https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token": self._token
        }
        r=self.post(url,params=params,)

ab=AddressBook()
ab.create(name="cosmos",userid=ab.get_uid())
ab.post()
abcd



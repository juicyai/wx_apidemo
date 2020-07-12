import logging

from wx_api.baseApi import BaseApi


class Member(BaseApi):
    # logging.basicConfig(level=logging.DEBUG)

    def create_(self,**kwargs):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        # params = {
        #     "access_token": self._token
        # }
        # logging.debug(params)
        if "email" not in kwargs:
            kwargs["email"]="{}@koki.com".format(self.get_uid())
        if "mobile" not in kwargs:
            kwargs["mobile"]=self.get_uid()
        self.log.info("kw:{}".format(kwargs))
        json = self.get_template("create_json", kwargs)
        self.log.info(json)
        self.source("member","create_").set_params().set_json(json).run()
        # r = self.post(url, params=params, json=paylaod)
        # print(r.status_code)
        # logging.debug(r.status_code)
        # logging.debug(r.json())
        # print(r.json())
        return self

    def get_(self,userid):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        # params = {
        #     "access_token": self._token,
        #     "userid": "userid"
        # }
        # logging.debug(params)
        #paylaod = self.get_template("create_body", kwargs)
        self.source("member", "get_").set_params(userid=userid).run()
        # r = self.get(url, params=params)
        # print(r.status_code)
        # logging.debug(r.status_code)
        # logging.debug(r.json())
        # print(r.json())
        return self
    def post_(self,**kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        params = {
            "access_token": self._token
        }
        logging.debug(params)
        paylaod = self.get_template("create_body", kwargs)
        r = self.post(url, params=params, json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r

    def delete_(self,**kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "access_token": self._token,
            "userid": "$userid"
        }
        logging.debug(params)
        paylaod = self.get_template("create_body", kwargs)
        r = self.post(url, params=params)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r

    def batchdelete(self,**kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        params = {
            "access_token": self._token
        }
        logging.debug(params)
        paylaod = {
                    "useridlist": ["zhangsan", "lisi"]
                  }
        r = self.post(url, params=params, json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r

    def simplelist(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist"
        params = {
            "access_token": self._token,
            "department_id": "userid",
            "fetch_child": ""
        }
        logging.debug(params)
        # paylaod = self.get_template("create_body", kwargs)
        r = self.get(url, params=params)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r

    def list(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/list"
        params = {
            "access_token": self._token,
            "department_id": "userid",
            "fetch_child": ""
        }
        logging.debug(params)
        # paylaod = self.get_template("create_body", kwargs)
        r = self.get(url, params=params)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r

    def convert_to_openid(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/convert_to_openid"
        params = {
            "access_token": self._token
        }
        logging.debug(params)
        paylaod = {
            "userid": "zhangsan"
                   }
        r = self.post(url, params=params, json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())
        return r
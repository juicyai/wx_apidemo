import json
import logging

from wx_api.baseApi import BaseApi
from wx_api.start import Start


class Department(BaseApi):

    # def __init__(self):
    #   super().__init__()

    def create_(self,json:dict): #需从外部传入参数
        #url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # params = {
        #     "access_token": self._token
        # }
        # logging.debug(params)
        # json = {
        #            "name": "广州研发中心",
        #            "name_en": "RDGZ",
        #            "parentid": 1,
        #            "order": 1,
        #            "id": 2
        #         }
        self.source("Department","create_").set_params().set_json(json).run()
        # r = self.post(url, params=params, json=json)
        # print(r.status_code)
        # logging.debug(r.status_code)
        # logging.debug(r.json())
        # print(r.json())
        self.log.info(str("return json:{}".format(self.response.json())))
        return self

    def update_(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        params = {
            "access_token": self._token
        }
        logging.debug(params)
        paylaod = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }

        r = self.post(url, params=params, json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())

    def delete_(self,id):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        # params = {
        #     "access_token": self._token,
        #     "id": "$id"
        # }
        # logging.debug(params)
        self.source("Department","delete_").set_params(id=id).run()
        # r = self.post(url, params=params)
        # print(r.status_code)
        # logging.debug(r.status_code)
        # logging.debug(r.json())
        # print(r.json())
        return self

    def list(self,id=None):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        # params = {
        #     "access_token": self._token,
        #     "id": "$id"
        # }
        # logging.debug(params)
        self.source("Department", "list").set_params(id=id).run()
        self.log.info("list jsonbody:{}".format(json.loads(json.dumps(self.response.json()))))
        # r = self.post(url, params=params, json=paylaod)
        # print(r.status_code)
        # logging.debug(r.status_code)
        # logging.debug(r.json())
        # print(r.json())
        return self

if __name__=="__main__":
    Start.start()
    # print(Department().create_().validate("status_code",200)
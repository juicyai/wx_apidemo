import logging

from wx_api.baseApi import BaseApi
from wx_api.start import Start


class Department(BaseApi):
    logging.basicConfig(level=logging.DEBUG)

    def create_(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
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
        return r

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

    def delete_(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {
            "access_token": self._token,
            "id": "$id"
        }
        logging.debug(params)

        r = self.post(url, params=params)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())

    def list(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {
            "access_token": self._token,
            "id": "$id"
        }
        logging.debug(params)

        r = self.post(url, params=params, json=paylaod)
        print(r.status_code)
        logging.debug(r.status_code)
        logging.debug(r.json())
        print(r.json())

if __name__=="__main__":
 Start.start()
 Department().create_()
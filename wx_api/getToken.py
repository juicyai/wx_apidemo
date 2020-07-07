import logging

import requests

from utils.parseYaml import ParseYaml


class GetToken:
    logging.basicConfig(level=logging.INFO)
    _token=""
    @classmethod
    def get_token(cls):
        corp=ParseYaml.readYaml("corp")["corp"]
        params={"corpid":corp["corpid"],
                "corpsecret":corp["corpsecret"]
                }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        logging.info(str(r.status_code))
        cls._token=r.json()["access_token"]
        logging.info(cls._token)
        return cls._token

import logging

import requests

from utils.parseYaml import ParseYaml


class SessionAndToken:
    logging.basicConfig(level=logging.INFO)
    _token=""
    session:requests.sessions.Session

    @classmethod
    def create_session(cls):
        cls.session = requests.session()
        return cls
    @classmethod
    def get_token(cls):
        corp=ParseYaml.readYaml("corp")["corp"]
        params={"corpid":corp["corpid"],
                "corpsecret":corp["corpsecret"]
                }
        r=cls.session.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        logging.info(str(r.status_code))
        cls._token=r.json()["access_token"]
        logging.info(cls._token)
        return cls

if __name__=="__main__":
    SessionAndToken.create_session()
    print(type(SessionAndToken.session))


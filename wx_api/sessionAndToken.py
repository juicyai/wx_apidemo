import logging

import requests

from utils.parseYaml import ParseYaml


class SessionAndToken:

    # logging.basicConfig(
    #     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
    #     datefmt='%m/%d/%Y %I:%M:%S %p',
    #     level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    _log = logging.getLogger("wx")
    _log.setLevel(level=logging.DEBUG)


    #使用类变量管理token和session,实现token和session共享
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
        cls._log.info(str(r.status_code))
        cls._token=r.json()["access_token"]
        logging.info(cls._token)
        return cls

if __name__=="__main__":
    SessionAndToken.create_session()
    print(type(SessionAndToken.session))


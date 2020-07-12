from wx_api.baseApi import BaseApi
from wx_api.sessionAndToken import SessionAndToken


class Start:
    @classmethod
    def start(cls):
        SessionAndToken.create_session().get_token()
        return BaseApi()



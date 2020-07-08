import requests


class IniSession:
    session:requests.sessions.Session
    @classmethod
    def create_session(cls):
        cls.session=requests.session()
        return cls.session


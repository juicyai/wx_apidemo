from testcase.baseCase import BaseCase
from wx_api.addressBook.department import Department
from wx_api.addressBook.member import Member
import pytest


class TestMember(BaseCase):

    @classmethod
    def setup_class(cls):
        cls.m = Member()
    @pytest.mark.parametrize("userid,name",[("zhangshan06","张山"),("xiayu06","夏雨")])
    def test_create(self,userid,name):

        j=self.m.create_(userid=userid,name=name).\
            validate("status_code",200).validate("json().errcode",0).\
            get_(userid).validate("status_code",200).\
            validate("json().userid",userid).\
            validate("json().name",name)
        self.log.info(j.response.json())

    @pytest.mark.parametrize("userid,errcode",[("zhangshan",0),("zhangsh",60111)])
    def test_get(self,userid,errcode):

        r=self.m.get_(userid).validate("status_code",200).\
            validate("json().errcode",errcode)
        errcode=r.response.json()["errcode"]
        if errcode:
           assert "userid not found" in r.response.json()["errmsg"]
    @pytest.mark.parametrize("departmentid,errcode",[(1,0),(100,60003)])
    def test_simplelist(self,departmentid,errcode):
        r=self.m.simplelist(department_id=departmentid).validate("status_code",200).\
            validate("json().errcode",errcode)
        if r.response.json()["errcode"]:
            assert "not found" in r.response.json()["errmsg"]
        self.log.info(r.response.json())
    @pytest.mark.parametrize("userid",["zhangshan","xiayu"])
    def test_convert_to_openid(self,userid):
        r=self.m.convert_to_openid(userid).validate("status_code",200)
        self.log.info(r.response.json())

    @pytest.mark.parametrize("code",[12,10000])
    def test_getuserinfo(self,code):
        self.m.getUserInfo(code).validate("status_code",200).validate("json().errcode",0)





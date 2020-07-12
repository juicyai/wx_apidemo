from testcase.baseCase import BaseCase
from wx_api.addressBook.department import Department
from wx_api.addressBook.member import Member
import pytest


class TestMember(BaseCase):

    @classmethod
    def setup_class(cls):
        cls.m = Member()
    @pytest.mark.parametrize("userid,name",[("zhangshan","张山"),("xiayu","夏雨")])
    def test_create(self,userid,name):

        j=self.m.create_(userid=userid,name=name).\
            validate("status_code",200).validate("json().errcode",0).\
            get_(userid).validate("status_code",200).\
            validate("json().userid",userid).\
            validate("json().name",name)
        self.log.info(j.response.json())

    @pytest.mark.parametrize("userid",["zhangshan"])
    def test_get(self,userid):

        j=self.m.get_(userid).validate("status_code",200).response.json()
        self.log.info(j)

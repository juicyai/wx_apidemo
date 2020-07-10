import json

import pytest
#from jsonschema import validate
from jsonpath import jsonpath
from hamcrest import *

from wx_api.addressBook.department import Department


class TestDepartment:

    @classmethod
    def setup_class(cls):
        cls.Department = Department()
    def setup_method(self):
        pass
    @pytest.mark.parametrize('name,parentid,errcode',
                             [("宇宙射线研究小组", 3,0),
                              ("Cosmic Ray Research Group", 3,0),
                              ("宇宙線研究グループ", 3,0),
                              ("Groupe de recherche sur les rayons cosmiques", 2,60001),
                              ("Groupe de recherche sur les rayo",2,0),
                              ("f",2,0),
                              ("f2","2",0),
                              ("",2,40058),
                              ("우주 광선 연구 그룹", 2,0),
                              ("مجموعة أبحاث الأشعة الكونية", 2,0)],
                             ids=["create_CN", "create_EN", "create_JP", "create_lg32name",
                                  "create_border_32","create_border_1","create_errTypeParentId",
                                  "create_ls1Name", "create_KR", "create_AR"])
    def test_create_nameLanguage(self, name, parentid,errcode):
        js = {
            "name": name,
            "parentid": parentid
        }
        errcode=self.Department.create_(js).\
            validate("status_code", 200). \
            validate("json().errcode", errcode).response.json()["errcode"]
        if errcode==0:
            s=self.Department.list().validate("status_code", 200).response.json()
            assert_that(jsonpath(json.loads(json.dumps(s)),"$.department[*].name"),has_item(name))
            assert_that(jsonpath(json.loads(json.dumps(s)),"$.department[*].parentid",has_item(parentid)))


    def test_list(self):
        s=self.Department.list().validate("status_code",200)
        j=s.response.json()
        print("j type:{}".format(type(j)))
        jsonpath(j,"$..")

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass


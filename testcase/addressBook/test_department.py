import json
import pytest,allure
from jsonpath import jsonpath
from hamcrest import *

from testcase.baseCase import BaseCase
from wx_api.addressBook.department import Department

@allure.description("department logic test")
@allure.severity("critical")
@allure.story("01_department")
@pytest.mark.departmentTest
class TestDepartment(BaseCase):

    @classmethod
    def setup_class(cls):
        cls.Department = Department()
    def setup_method(self):
        pass
    @allure.severity("critical")
    @allure.testcase("https://baidu.com")
    @allure.issue("https://baidu.com")
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

    @allure.severity("major")
    @allure.testcase("https://baidu.com")
    @allure.issue("https://baidu.com")
    def test_list(self):
        s=self.Department.list().validate("status_code",200)
        j=s.response.json()
        self.log.info("j type:{}".format(j))
        print("j type:{}".format(type(j)))
        # jsonpath(j,"$..")

    @allure.severity("critical")
    @allure.testcase("https://baidu.com")
    @allure.issue("https://baidu.com")
    @pytest.mark.parametrize("id,expectCode,expectMsg",
                             [(1000,60123,"invalid party id"),
                              (10,0,"deleted")
                              ],ids=["delete_fail","delete_success"])
    def test_delete(self,id,expectCode,expectMsg):
        r=self.Department.delete_(id)
        errcode=r.validate("status_code",200).\
            validate("json().errcode",expectCode)
        assert expectMsg in r.response.json()["errmsg"]
        if errcode==0:
            j = self.Department.list().validate("status_code", 200).response.json()
            assert id not in jsonpath(json.loads(json.dumps(j)), "$.department[*].id")





    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass


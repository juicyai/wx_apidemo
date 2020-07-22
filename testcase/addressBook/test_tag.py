import pytest

from testcase.baseCase import BaseCase
from wx_api.addressBook.tag import Tag


class TestTag(BaseCase):
    @classmethod
    def setup_class(cls):
        cls.tag=Tag()

    @pytest.mark.parametrize("tagname,tagid",[("",10),
                                              ("u",11),
                                              ("abcdefghijklmnopqrstuvwxyzabcdef",12),
                                              ("_#$abdc",13),
                                              ("1234",14),
                                              ("هذه علامة",15),
                                              ("我和我的祖国像海浪和花一朵无论你走到哪里都来留下一首赞歌",16)
                                              ],ids=["name_null","name_1","name_32","name_special",
                                                     "name_number","name_arb","name_CN"])
    def test_create(self,tagname,tagid):
        self.tag.create(tagname,tagid).validate("status_code",200).validate("json().errcode",0)



import pytest

from testcase.baseCase import BaseCase


class TestMedia(BaseCase):
    fields=("file",)
    @pytest.mark.parametrize("fields,type",[(())])
    def test_upload(self,fields,type):

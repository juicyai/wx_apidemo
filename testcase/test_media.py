import pytest,allure

from testcase.baseCase import BaseCase

@allure.description("media logic test")
@allure.story("04_media_logic")
class TestMedia(BaseCase):
    fields=("file",)

    #@pytest.mark.parametrize("fields,type",[(())])
    @pytest.mark.skip
    def test_upload(self,fields,type):
        pass

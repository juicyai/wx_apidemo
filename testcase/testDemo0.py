import requests,logging,json,pytest
from jsonpath import *
from hamcrest import *
class TestDemo01:
    def test_01(self):
        #logging.basicConfig(level="INFO")
        params={"category": "1"}
        url="https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json"
        cookies={"xq_a_token":
                     "f3646a14c8cc784b6ca2ddfaabfc34cbd6d36e86",
                 "u": "5261478148"
                }
        header={
                "Host": "stock.xueqiu.com",
                "User-Agent": "Xueqiu Android 12.8.1"
               }
        r=requests.get(url,headers=header,params=params,cookies=cookies)
        print(r.status_code)
        logging.info(str(r.status_code))
        logging.info(json.dumps(r.json(),indent=2))
        assert_that(jsonpath(r.json(),"$..name"),any_of(has_item("招商银行"),has_item("中国平安")))
        assert "招商银行" or "中国平安" in jsonpath(r.json(),"$..name")

    def test_demo(self):
        r=requests.get("http://www.baidu.com")
        print(r.status_code)



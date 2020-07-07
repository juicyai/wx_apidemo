import requests


def test_1():
    r=requests.get("http://www.baidu.com")
    print(r.status_code)
    assert r.status_code==200
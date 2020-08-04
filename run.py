import os

import pytest

if __name__=="__main__":
    pytest.main(['-s','-q','--alluredir','./reports/allure-result'])
    os.system("allure generate ./reports/allure-result -o ./reports/allure-report --clean")
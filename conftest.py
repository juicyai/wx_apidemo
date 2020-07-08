
import pytest

from wx_api.iniSession import IniSession


@pytest.fixture(scope="session",autouse=True)
def ini_session():
    IniSession.create_session()
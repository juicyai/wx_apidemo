
import pytest

from wx_api.start import Start

"""参数共享"""

@pytest.fixture(scope="session",autouse=True)
def start_():
    Start.start()

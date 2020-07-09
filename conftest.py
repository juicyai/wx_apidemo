
import pytest

from wx_api.start import Start

"""参数共享"""

@pytest.fixture(scope="session",autouse=False)
def start_():
    Start.start()


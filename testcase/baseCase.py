import logging

import pytest

from wx_api.start import Start



class BaseCase:

        # logging.basicConfig(
        #     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
        #     datefmt='%m/%d/%Y %I:%M:%S %p',
        #     level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        _log=logging.getLogger("wx")
        _log.setLevel(level=logging.DEBUG)
        @property
        def log(self):
            return self._log






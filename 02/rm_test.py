# With Mocks
from rm import rm


import mock
import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('rm.os')
    def test_rm(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")
        
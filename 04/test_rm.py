from rm_module import RemoveService

import unittest
import mock

class RemoveServiceTestCase(unittest.TestCase):

    @mock.patch('rm_module.os.path')
    @mock.patch('rm_module.os')
    def test_rm(self, mock_os, mock_path):
        # Create instance of service
        service = RemoveService()

        # Create mock
        mock_path.isfile.return_value = False

        service.rm("any path")

        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present")

        mock_path.isfile.return_value = True
        
        service.rm("any path")

        mock_os.remove.assert_called_with("any path")
        
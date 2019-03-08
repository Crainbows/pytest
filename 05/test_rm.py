from rm_module import RemoveService, UploadService

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
        
class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemoveService)
        reference = UploadService(mock_removal_service)
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")
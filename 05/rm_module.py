import os
import os.path

class RemoveService(object):


    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):

    def __init__(self, removal_service):
        self.RemoveService = removal_service

    def upload_complete(self, filename):
        self.RemoveService.rm(filename)
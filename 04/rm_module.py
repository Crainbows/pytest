import os
import os.path

class RemoveService(object):


    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
import tempfile
import os
class TemporaryFile:
    def __enter__(self):
        self.fd, self.path = tempfile.mkstemp()
        return self.path
    def __exit__(self, exception, error, traceback):
        os.remove(self.path)

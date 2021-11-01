import tempfile
import os
class TemporaryDirectory:
    def __enter__(self):
        self.path = tempfile.mkdtemp()
        return self.path
    def __exit__(self, exception, error, traceback):
        os.rmdir(self.path)
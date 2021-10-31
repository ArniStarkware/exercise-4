from io import StringIO  # Python 3
import sys

class StandardOutput:
    def __enter__(self):
        self.string_writer = StringIO()
        sys.stdout = self.string_writer
        return self
    def __exit__(self, exception, error, traceback):
        self.value = self.string_writer.getvalue()
        sys.stdout = sys.__stdout__
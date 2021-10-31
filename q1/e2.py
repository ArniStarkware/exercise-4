from attr import set_run_validators


class Suppress:
    def __enter__(self):
        pass
    def __init__(self, *args):
        self.exceptions = args
    def __exit__(self, exception, error, traceback):
        if len(self.exceptions) == 0 or exception in self.exceptions:
            return True

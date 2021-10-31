import time
class Timer:
    def __enter__(self):
        self.started = time.time()
        return self
    def __exit__(self, exception, error, traceback):
        self.stopped = time.time()
        self.elapsed = self.stopped - self.started


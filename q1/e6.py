from contextlib import suppress
from os import path


class ContextManager:
    def __init__(self,generator) -> None:
        self.generator = generator
    
    def __enter__(self):
        self.execution = self.generator()
        return next(self.execution)
    def __exit__(self, exception, error, traceback):
        with suppress(StopIteration):
            if exception:
                self.execution.throw(exception)
            else:
                next(self.execution)

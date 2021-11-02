import contextlib
import time
from io import StringIO 
import sys
import tempfile
import os

@contextlib.contextmanager
def timer():
    started = time.time()
    class timerObject:
        def __init__(self) -> None:
            self.started = started
    retObj = timerObject()
    try:
        yield retObj
    finally:
        stopped = time.time()
        elapsed = stopped - started
        retObj.stopped = stopped
        retObj.elapsed = elapsed

@contextlib.contextmanager
def suppress(*exceptions):
    if exceptions:
        try:
            yield
        except exceptions:
            pass
    else:
        try:
            yield
        except:
            pass


@contextlib.contextmanager
def standard_output():
    class stdoutObject:
        def __init__(self) -> None:
            self.string_writer = StringIO()
    retObj = stdoutObject()
    sys.stdout = retObj.string_writer
    yield retObj
    retObj.value = retObj.string_writer.getvalue()
    sys.stdout = sys.__stdout__

@contextlib.contextmanager
def temporary_file():
    _ , path = tempfile.mkstemp()
    yield path
    os.remove(path)

@contextlib.contextmanager
def temporary_directory():
    path = tempfile.mkdtemp()
    yield path
    os.rmdir(path)

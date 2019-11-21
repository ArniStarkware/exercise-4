import threading
import time

import pytest

from e7 import Extended


def test_sync():
    x = []
    class A(metaclass=Extended):
        def f(self):
            time.sleep(0.1)
            x.append(1)
    a = A()
    t1 = threading.Thread(target=a.f)
    t2 = threading.Thread(target=a.f)
    t1.start()
    t2.start()
    assert len(x) == 0
    time.sleep(0.15)
    assert len(x) == 2
    x = []
    t1 = threading.Thread(target=a.f_sync)
    t2 = threading.Thread(target=a.f_sync)
    t1.start()
    t2.start()
    assert len(x) == 0
    time.sleep(0.15)
    assert len(x) == 1
    time.sleep(0.1)
    assert len(x) == 2


def test_safe():
    class A(metaclass=Extended):
        def f(self):
            raise ValueError()
    a = A()
    with pytest.raises(ValueError):
        a.f()
    a.f_safe()

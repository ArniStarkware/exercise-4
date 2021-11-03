import threading

class Extended(type):
    def __init__(cls, name, bases, attrs):
        cls.lock = threading.Lock()
        newAttrs = {}
        for key, value in attrs.items():
            if callable(value):
                threadSafeMethod = createThreadSafeMethod(value, cls.lock)
                exceptionSafeMethod = createExceptionSafeMethod(value)
                newAttrs[key + '_sync'] = threadSafeMethod
                newAttrs[key + '_safe'] = exceptionSafeMethod
        for key, value in newAttrs.items():
            setattr(cls,key,value)

def createThreadSafeMethod(f, lock):
    def f_locked(*args, **kwargs):
        with lock:
            return f(*args,**kwargs)
    return f_locked
def createExceptionSafeMethod(f):
    def f_safe(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            pass
    # do we want to set something in this f? so it will feel like it belongs to the class, not just the extended class?
    return f_safe


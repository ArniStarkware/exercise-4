from typing import Dict


class Overloaded(type):
    def __prepare__(mcs, name, bases= None):
        
        return OverloaderDict()
class OverloaderDict(dict):
    def __init__(self) -> None:
        pass

    def __setitem__(self, key, value):
        if callable(value):
            if key not in self:
                overloader = Overloader()
                super().__setitem__(key,overloader)
            overloader = super().__getitem__(key)
            overloader.addSign(value)
        else:
            super().__setitem__(key, value)

class Overloader():
    def __init__(self):
        self.lst = []
    def isNeeded(self):
        return bool(self.lst)
    def addSign(self,value):
            # need to have more logic - make sure no other 
            # element in the list has same signature
        if all(True for met in self.lst):
            self.lst.append(value)
    def __call__(self, *args, **kwds):
        for method in self.lst:
            try:
                output = method.__call__(method, *args, **kwds)
                return output
            except TypeError:
                pass
        raise TypeError()

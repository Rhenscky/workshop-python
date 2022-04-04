import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                  
d = weakref.WeakValueDictionary()
d['primary'] = a           
d['primary']               

del a                      
gc.collect()               

d['primary']               

'''
See http://current.blogspot.ca/2014/09/private-variables-in-python.html
for a better method of data hiding using closures
'''


class Test:
    def __init__(self):
        self.publicVar = 0
        self._protectedVar = 1
        self.__privateVar = 2
        self.__anotherPrivateVar_ = 3
        self.__isThisAPrivateVar__ = 4  # No
        

    def publicMethod(self):
        print 'Public Method'
        
    def _protectedMethod(self):
        print 'Protected Method'

    def __privateMethod(self):
        print 'Private Method'

    def __anotherPrivateMethod_(self):
        print 'Another Private Method'

    def __isThisAPrivateMethod__(self):
        print 'This is not a Private Method'

t = Test()
print t.publicVar
print t._protectedVar
print t._Test__privateVar
print t._Test__anotherPrivateVar_
print t.__isThisAPrivateVar__

t.publicMethod()
t._protectedMethod()
t._Test__privateMethod()
t._Test__anotherPrivateMethod_()
t.__isThisAPrivateMethod__()



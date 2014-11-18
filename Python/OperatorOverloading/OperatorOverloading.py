# Comment


class NewString(str):
    pass
    '''
    def __init__(self, s):
        super(s)
    '''

    def __add__(self, other):
        return self.__str__() + self.__str__() + ' ' + other + other

    def __eq__(self, other):
        return True

    def __mul__(self, other):
        return (self+' ')*other

x = NewString('aaa')
y = NewString('bbb')

# Comment

print x+y
print x*2 + y*3

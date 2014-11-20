
import ctypes

testlib = ctypes.CDLL('./libtest.so')
#x = testlib._Z7myprintv()
x = testlib.myprint()
print 'return value: ', x

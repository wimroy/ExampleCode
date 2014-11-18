'''
Run with 'python -O' to set __debug__ to false
'''

def gen1(n=10):
    i = 1
    result = []
    while i <= n:
        if __debug__:
            print 'x',
        result.append(i)
        i += 1
    if __debug__:
        print
    return result


def gen2(n=10):
    i = 1
    while i <= n:
        if __debug__:
            print 'y',
        yield i
        i += 1
    if __debug__:
        print

print gen1(10)
print gen2(10)

for i in gen1(10):
    if i == 5:
        break
    print i,

print

for i in gen2(10):
    if i == 5:
        break
    print i,

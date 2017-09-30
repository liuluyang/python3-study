

def fib(n):
    l = []
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
        l.append(a)
    return l

print (fib(10))

def fib_2(n):
    a,b = 0,1
    m = 0
    while m<n:
        a,b = b,a+b
        m+=1
        yield a

print (fib_2(10))
for i in fib_2(10):
    print (i)
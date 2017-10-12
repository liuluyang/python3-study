
def visit(data):
     for elem in data:
         if isinstance(elem, tuple) or isinstance(elem, list):
             #yield from visit(elem)
            for i in visit(elem):
                yield i
         else:
             yield elem

for i in visit([1,2,[3,4,(11,22)],5]):
    print (i)
###########################################################
def ge(num):
    if num<0:
        return
    else:
        for i in range(num):
            yield i

print (next(ge(1)))


############################################################

l = []
def vist(data):
    for i in data:
        if isinstance(i, (tuple, list)):
            vist(i)
        else:
            l.append(i)
    return l

print (vist([1,2,[3,4,(11,22)],5]))
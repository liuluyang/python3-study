
def triangles():
    yield [1]
    l = [1, 1]
    yield l
    while True:
        l = [1]+[l[n]+l[n+1] for n in range(len(l)-1)]+[1]
        yield l
t = triangles()
for i in range(7):
    print (next(t))

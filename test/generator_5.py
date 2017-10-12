def gen(n):
    while n >= 0:
        num = yield n
        if num is not None:
            #print (num)
            n = num
        else:
            n -= 1


if __name__ == '__main__':
    g = gen(5)
    for i in g:
        print(i)
        if i == 5:
            t = g.send(3)
            #print (t)
        if i == 2:
            g.send(1)



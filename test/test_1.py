

def money(base,rate):
    m = base
    while True:
        m = m + m*rate
        yield m


m = money(150000, 0.12)
#m.send(None)
for i in range(10):
    print (next(m))

def money_2(base, rate):
    m = base
    while True:
        m = m + m*rate + base
        yield m

m2 = money_2(50000, 0.1)
#for y in range(10):
    #print (next(m2))
for x,y in enumerate(range(10)):
    print (x+1,'年', next(m2))

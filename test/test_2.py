print (abs(10))

__n__ = 'name'
print (__n__)

class Mode(object):
    def __init__(self):
        self.name = 'llu'
    def __getattr__(self, item):
        print ('st')
        if item == 'name':
            return 'lo'

m = Mode()
print (m.nam)

class M(dict):
    def __init__(self,**kwargs):
        super(M, self).__init__(**kwargs)
    def __getattr__(self, key):
        try:
            print ('tyr')
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        print ('set')
        self[key] = value

m = M(id=1)
print (m.id)
#m.name = 2
m['nam'] = 3
print (m.nam)
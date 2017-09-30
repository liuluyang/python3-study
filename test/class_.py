
class Animal(object):
    def run(self):
        print ('animal is running')

class Dog(Animal):
    def run(self):
        print ('dog is running ')

class D(Dog):
    pass

d = D()
d.run()
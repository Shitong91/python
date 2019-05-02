class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(ani):
    ani.run()
    ani.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a,Animal))
print('a is Dog', isinstance(a, Dog))

print('d is Animal?', isinstance(d, Dog))
print('d is Dog?', isinstance(d, Dog))

run_twice(c)


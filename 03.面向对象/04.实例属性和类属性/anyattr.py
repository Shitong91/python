class Student(object):
    def __init__(self, name):
        self.name=name

s = Student('Bob')
s.score = 90

t = Student(20)
print(t.score)

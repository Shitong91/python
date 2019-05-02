#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass
s = Student()
s.name = 'Michael'
print(s.name)
# 以上是给予属性的动态绑定

def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age) # 基于方法的动态绑定,仅对当前的实例有作用


def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)
s2=Student()
s2.set_score(99)
print(s2.score)
# 基于类的方法绑定

class Student_t(object):
    __slots__ = ('name', 'age')
s3 = Student_t()
s3.name = 'Michael'
s3.age = 25
s3.score = 99 #不包括在slots里，所以这个定义是无效的


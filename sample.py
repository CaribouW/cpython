import copy
import numpy as np
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __reduce__(self):
        return (self.__class__, (self.name)) # 只序列化 name 属性
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

li = np.array([[1, 2, 3], [4, 5, 6]])
# li = [[1, 2, 3], [4, 5, 6]]

new_ele = li[0][0]
tID = id(new_ele)
# Note: please do not include operations (e.g. slicing) in `id_deref`
print('deref', id_deref(tID, type(new_ele)))
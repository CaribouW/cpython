import copy
import numpy as np

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __reduce__(self):
        return (self.__class__, (self.name)) # 只序列化 name 属性
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

obj = [3,4]
obj = np.array([[1, 2, 3], [4, 5, 6]])

print(hex(id(obj)))
new_obj = copy.heapsize(obj)
print(new_obj,hex(id(new_obj)))

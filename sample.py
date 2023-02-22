# import numpy as np
# import pickle
# # create a numpy array
# my_array = np.array([1, 2, 3, 4, 5])

# # print the array
# print(hex(id(my_array)))
# print(hex(id(my_array[0])))

# print(pickle.dumps(my_array))
obj = True
print(hex(id(obj)))
i = id(obj)
print(id_deref(i))

print(heapize(obj))
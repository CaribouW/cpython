import time
li = []
li.append('hello')
li.append(3)
di = {"4":342}
tmp = set(li)
str1 = "Python1"
str2 = "Python2"
int1 = 1234
print(id(str1), hex(id(str1)))
print(id(str2), hex(id(str2)))
print(id(li[0]), hex(id(li[0])))
print(id(li[1]), hex(id(li[1])))

print(id(li), hex(id(li)))
print(id(di), hex(id(di)))
print(id(di['4']), hex(id(di['4'])))
print(id(tmp), hex(id(tmp)))
print(id(int1), hex(id(int1)))

t = id(li)
print(id_deref(t))
print(id_deref(id(li)))

# BASE_HEX=4ffff5a00000 TOTAL_SZ_HEX=40000000 LD_PRELOAD=/home/lfm/libmalloc_wrapper.so ./python sample.py



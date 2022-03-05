# 面试体
t1 = (1, 2, 3)
t2 = (1, 2, 3)

t3 = {1,2,3}
t4 = {1,2,3}

t3[1] = 5

s1 = "ABC"
s2 = "ABC"

a = None
b = None

print(id(a))
print(id(b))

print(id(t1))
print(id(t2))

print(t2 is t1)
print(t1 == t2)

print(s1 == s2)
print(s1 is s2)

print(t3 == t4)
print(t3 is t4)

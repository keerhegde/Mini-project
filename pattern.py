import copy
s1=[123, 'str', 'abc']
s2=s1
print(s2)
s1.append(999)
print(id(s1))
print(id(s2))
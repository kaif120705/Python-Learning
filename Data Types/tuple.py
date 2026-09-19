print("==" * 25)
print("==" * 8, "Empty tuple","==" *8)
a=() # Declaration of tuple
print(a,type(a))
b=tuple() # Declaration of tuple
print(b,type(b))
print("==" * 25)
print("==" * 8, "NON-Empty tuple","==" *7)
a=23,10,20,10,"Mumbai",2+5j # Declaration of tuple
print(a,type(a))
b=tuple(a) # Declaration of tuple
print(b,type(b))
a=(23,10,20,10,"Mumbai",2+5j) # Declaration of tuple
print(a,type(a))
b=(23)
print(b,type(b)) # here the val stored in b is int type
b=(23,)
print(b,type(b)) # here the val stored in b is tuple type
print("==" * 25)
t=10,20,30,"kaif",3+5j
print(t,type(t))
print(t[0])
print(t[-1])
print(t[len(t)-1])
print(t[-len(t)])
print(t[1:5])
print(t[::2])
print(t[-2:-4:-1])
print(t[::-1])
#t[1]=3 #TypeError: 'tuple' object does not support item assignment
#print(t)
print("==" * 25)
print("==" * 9, "Conversion","==" *9)
s="ABRAKADABRA"
print(tuple(s))
l1=[10,20,30,2+5j]
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))
r1=tuple(range(0,10,2))
print(r1,type(r1))
#a=22
#print(type(a),type(tuple(a)))
t=22, # or (22,)
print(t,type(t))
t=22
t1=[22]
t2=tuple(t1)
print(t2,type(t2))
print("==" * 25)
print("==" * 7, "Pre-defined Function","==" *7)
print("==" * 7, "Index & count","==" *7)
t=(10,20,30,"kaif",3+5j)
print(t.index(30),type(t))
print(t.count("kaif"),type(t))
t=10,20,30,10,40,10,20,10,20
print(t,type(t))
print(t.count(10),type(t))
print(t.count(20),type(t))
print("==" * 25)
t1=(10,20,30,"kaif",3+5j)
print(t1,type(t1),id(t1))
#t1=t.copy() AttributeError: 'tuple' object has no attribute 'copy'
t2=t1
print(t2,type(t2),id(t2))
print("==" * 25)
print("==" * 7, "del operator on tuple","==" *7)
t=(10,20,30,"kaif",3+5j)
print(t,type(t))
#del t[10] TypeError: 'tuple' object doesn't support item deletion
del t
# print(t,type(t)) NameError: name 't' is not defined.
# NOTE: By using del operator we can't delete value of tuple but we can delete entire tuple object
print("==" * 25)
print("==" * 6, "M IMP-sorted(tuple obj)","==" *6)
# NOTE: sorted() is used for sorting the data of IMMUTABLE Obj and gives the sorted data in the fotm of LIST
t1=(90,10,76,34,24,67,58,97)
print(t1)
t2=sorted(t1) # This will gives result in the form of LIST [10, 24, 34, 58, 67, 76, 90, 97]
print(t2,type(t2))
print(t2[::-1])
print("==" * 6, "sort the tuple","==" *6)
t1=(90,10,76,34,24,67,58,97)
print(t1)
l1=list(t1)
l1.sort()
print(l1,type(l1))
t=tuple(l1)
print(t,type(t))
print(t[::-1])
print("==" * 25)
print("==" * 6, "Nested/inner tuple","==" *6)
t1=(10,"Kaif",20,(16,17,18),(68,80,78),"Mumbai")
print(t1)
for val in t1:
    print(val,"-->",type(val),"-->",type(t1))
print(t1[3][1])
print(t1[-2][-2])
print("==" * 6, "list in tuple","==" *6)
t1=(10,"Kaif",20,[16,17,18],[68,80,78],"Mumbai")
print(t1,type(t1))
print(t1[3],type(t1[3]))
t1[-2].append(65)
print(t1,type(t1))
t1[3].insert(10,20)
print(t1,type(t1))
t1[-2].sort()
print(t1,type(t1))
t1[-2].sort(reverse=True)
print(t1,type(t1))
# print(t1.pop(10)) AttributeError: 'tuple' object has no attribute 'pop'
# del t1[0]  TypeError: 'tuple' object doesn't support item deletion
del t1[3][1]
print(t1,type(t1)) # 17 is removed
# NOTE: we can do the modification on list but we can't do any modification on overall list
# Bcoz its an element of tuple
print("==" * 6, "list in tuple","==" *6)
t1=[10,"Kaif",20,(16,16,19,18),(68,80,78),"Mumbai"]
for val in t1:
    print(val,"-->",type(val),"-->",type(t1))
# print(t1[3].append(5)) AttributeError: 'tuple' object has no attribute 'append'
print(sorted(t1[3]))
print(t1[3].count(16))
print(sorted(t1[3])[::-1])
t1[3]=sorted(t1[3])[::-1]
print(t1,type(t1))
t1.append("Maharashtra")
print(t1,type(t1))
# NOTE:
# One can define one list in another list
# One can define one tuple in another tuple
# One can define one list in another tuple (tuple of Lists)
# One can define one tuple in another list (Lists of tuple)

# set Category data types only store Unique values {}
# object of set belongs to both MUTABLE (we can do changes on same addr.) and IMMUTABLE because
# set never allows to perform an item Assignment
print("==" * 25)
s1={10,20,30,40,20,10,30} # storing only unique values
print(s1,type(s1))
s2={10,"HTML","CSS","JavaScript","Python","HTML"}
print(s2,type(s2))
print("==" * 25)
print("==" * 5, "MUTABLE and IMMUTABLE property","==" *5)
s1={10,"HTML","CSS","JavaScript","Python","HTML"}
# s1[1]=30 TypeError: 'set' object does not support item assignment IMMUTABLE
print(s1,type(s1),id(s1))
s1.add("SQL")
print(s1,type(s1),id(s1)) # the element will be added at same memory address thats why MUTABLE
print("==" * 25)
print("==" * 5, "Empty and Non Empty Set","==" *5)
s=set()
print(s,type(s))
print(len(s))
s1={10,20,30,40,20,10,30}
print(s1,type(s1))
print(len(s1))
print("==" * 25)
print("==" * 25)
print("==" * 3, "To find the unique elements from list or str","==" *3)
lst=[10,20,10,20,30,40,50]
print(lst,type(lst))
s=set(lst)
print(s,type(s))
st='MISSISSIPPI'
print(s,type(s))
s=set(st)
print(s,type(s))
print("==" * 25)
print("==" * 5, "Pre-Defined Functions in set()","==" *5)
print("==" * 8, "1-add()","==" *8)
s=set()
print(s,type(s),id(s))
s.add(10)
s.add(34.56)
s.add("mumbai")
s.add("Python")
print(s,type(s),id(s))
s1={'Python', 10, 34.56, 'mumbai'}
print(s1,type(s1),id(s1))
s1.add("Imteyaz")
print(s1,type(s1),id(s1))
print("==" * 25)
print("==" * 8, "2-remove(value)","==" *8)
s1={10,20,30,40,20,10,30}
print(s1,type(s1))
s1.remove(20)
print(s1,type(s1))
#s1.remove("Imteyaz") KeyError: 'Imteyaz' we are trying to remove those element which are not
# present in set
s1.remove(10)
s1.remove(30)
s1.remove(40)
print(s1,type(s1))
# s1.remove(40) KeyError: 40 bcoz set is empty
print("==" * 25)
print("==" * 8, "3-discard(value)","==" *8)
s={10, 'Python', 34.56, 'mumbai'}
print(s,type(s))
s.discard("Python")
print(s,type(s))
s.discard("Imteyaz") # No Error will come the o/p display shows no error
# s.remove("Imteyaz") KeyError: 'Imteyaz'
set().discard("Imteyaz") # No Error will come the o/p display shows no error
# set().remove("Imteyaz")  KeyError: 'Imteyaz'
print("==" * 25)
print("==" * 8, "4-pop()","==" *8)
s1={10,20,30,40}
# this func is used for removing any ARBITARY ELEMENT frm set obj provided NO ORDER OF DISPLAY
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
# print(s1.pop()) KeyError: 'pop from an empty set'
# set().pop() KeyError: 'pop from an empty set'
s1={10,20,30,40}
print(s1,type(s1))
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
# print(s1.pop()) KeyError: 'pop from an empty set'
print("==" * 25)
print("==" * 8, "5-clear()","==" *8)
s1={10,20,30,40}
print(s1,type(s1))
s1.clear()
print(len(s1))
print(s1,type(s1))
print(s1.clear())
print("==" * 25)
print("==" * 8, "6-isdisjoint()","==" *8)
# This gives TRUE if there is no common element else if there is one common element then gives False
s1={10,20,30,40}
s2={50,60,70}
s3={10,80,90}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))
s1=set()
s2=set()
print(s1.isdisjoint(s2))
print(set().isdisjoint(set()))
print(set().isdisjoint({10,20,30,40}))
print("==" * 25)
print("==" * 8, "7-issuperset()","==" *8)
# This func returns TRUE if setobj1 contains all the elements of setobj2
s1={10,20,30,40}
s2={30,40}
s3={70,80,10}
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(set().issuperset(set()))
print("==" * 25)
print("==" * 8, "8-issubset()","==" *8)
s1={10,20,30,40}
s2={10,20,30,40,50,60}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(set().issubset({10,20,50,60}))
print(set().issubset(set()))
print({10,20,50,60}.issubset(set()))
print("==" * 25)
print("==" * 8, "9-union()","==" *8)
# This Func is used for obtaining Unique values of setobj1 and setobj2 & place in setobj3
s1={10,20,30,40}
s2={10,20,60,70}
s3=s1.union(s2)
print(s3)
print(s1.union(s2))
s1={"C","JAVA","PYTHON"}
s2={"HTML","JAVA","PYTHON","CSS"}
s3=s1.union(s2)
print(s3)
print("==" * 25)
print("==" * 8, "10-intersection()","==" *8)
# This Func is used for obtaining Common elements form setobj
s1={10,20,30,40}
s2={10,60,70,20}
s3=s1.intersection(s2)
print(s3)
s1={"C","JAVA","PYTHON"}
s2={"HTML","JAVASCRIPT","DJANGO","CSS"}
s3=s1.intersection(s2)
print(s3) # IMP- IF NO COMMON ELEMENT IS PRESENT THEN IT WILL RETURN EMPTY SET set()
print("==" * 8, "IMP Question","==" *8)
s1={10,20,30,40}
s2={10,60,70,20}
s3={1,2,"python"}
print(s1,s2,s3,sep="\n")
print("s1.intersection(s2,s3)")
s4=s1.intersection(s2,s3)# it will give an EMPTY set()
print(s4) # because s1 intersection with s2 give {20,10} but s2 intersection with s3 it will give empty set
print("==" * 25)
print("==" * 8, "11-difference()","==" *8)
s1={10,20,30,40}
s2={10,60,70,20,70,90}
s3=s1.difference(s2)
print(s3)
s3=s2.difference(s1)
print(s3)
x={"python","HTML","CSS"}
y={"JAVASCRIPT","DJANGO","NUMPY"}
z=x.difference(y)
print(z)
z=y.difference(x)
print(z)
s1={10,20,30,40}
s2={10,20,30,40}
s3=s1.difference(s2)
print(s3)
print("==" * 25)
print("==" * 7, "12-symmetric_difference()","==" *7)
# This Func removes the common element and takes remaining elements from voth sets and place them in other variable
# setobj1.symmetric_difference(setobj2)
# setobj1.union(setobj2).difference(setobj1.intersection(setobj2))
a={10,20,30,78,68}
b={50,70,90,10,80,20,40}
c=a.symmetric_difference(b)
print(c)
s1={10,20,30,40}
s2={10,20,30,40}
s3=s1.symmetric_difference(s2)
print(s3)
s1={10,20,30,40,52,55}
s2={10,40,50,90,10,70}
s3=s1.union(s2).difference(s1.intersection(s2))
print(s3)
print("==" * 25)
print("==" * 8, "13-update()","==" *8)
# This Func is used for adding or merging of setobj2 with setobj1 and store them in setobj1
s1={10,20,30,40}
s2={50,60,70,80}
s1.update(s2)
print(s1)
s1={10,20}
s2={10,20}
s1.update(s2)
print(s1)
s1=set()
s1.update({10,20,30,40})
print(s1)
print("==" * 25)
print("==" * 5, "14-symmetric_difference_update()","==" *5)
s1={10,20,30,40}
s2={10,20,35,45}
s3=s1.symmetric_difference(s2)
print(s3)
del s3
print("==" * 25)
print("==" * 8, "IMP Question","==" *8)
set1={"Rohit","Kohli","Dhoni"} # Cricket Player
set2={"Messi","Ronaldo","Dhoni"} # Football Player
set3=set1.union(set2)
print(set3)
set3=set1.intersection(set2)
print(set3)
set3=set1.difference(set2)
print(set3)
set3=set2.difference(set1)
print(set3)
set3=set1.intersection(set2)
print(set3)
print("==" * 25)
print("==" * 8, "Nested/INNER sets","==" *8)
# case1: It is not possible to define one set in another set bcoz sets are unhashable type
# (Not Possible indexing and slicing)
# s1={"Rohit","Kohli","Dhoni",{"Messi","Ronaldo","Dhoni"}}
# print(s) TypeError: cannot use 'set' as a set element (unhashable type: 'set')
# case2: It is not possible to define one List in another set bcoz sets are unhashable type
# (Not Possible indexing and slicing)
# s2={"Rohit","Kohli","Dhoni",["Messi","Ronaldo","Dhoni"]}
# print(s) TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# case3: It is possible to define one tuple in another set bcoz tuples are IMMUTABLE
s3={"Rohit","Kohli","Dhoni",(10,20,"Kaif")}
print(s3)
for val in s3:
    print(val,type(val))
# case4: It is possible to define one set in another List bcoz List are MUTABLE and allows us to
# locate set objects by using indices.
s4=["Rohit","Kohli","Dhoni",{10,20,"Kaif"}]
print(s4)
print(s4[3],type(s4[3]))
s4[3].add(2+5j)
print(s4)
# case5: It is possible to define one set in another tuple bcoz tuples are IMMUTABLE and allows
# locate set objects by using indices.
s5=("Rohit","Kohli","Dhoni",{10,20,"Kaif"})
print(s5,type(s5))
print(s5[3],type(s5[3]))
s5[-1].add(50)
print(s5)
s5[-1].remove("Kaif")
print(s5)
print("==" * 25)
print("==" * 7, "Convert (-452) to (-254)","==" *7)
a=-453
print(a)
b=str(a)[1:]
print(b)
c=b[::-1]
print(c)
d=int(c)
print(d)
print(d*(-1))
print("-" + c)

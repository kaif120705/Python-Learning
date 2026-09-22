# Day-08
# Topic- list (collection) category data type
# Done By - Mohammad Kaif Alam
#=======================================================================
# The purpose list cat data types is "To store multiple values of
# same, different or both types in single obj with UNIQUE and DUPLICATES".
#========================================================================
print("==" * 25)
lst1=[10,20,10,20,30,40,50]
print(lst1,type(lst1))
lst=[10,"Kaif",True,5.4,2+3j]
print(lst,type(lst))
#==================================
# performing Indexing and Slicing
#==================================
print(lst[-1]) # Negative indexing
print(lst[len(lst)-1]) # gives last element
print([lst1[-len(lst1)]]) # gives 1st element by formula
print(lst1[2:6])
print(lst1[::-2])
print(lst[1::2])
print("==" * 25)
#=======================================================================================
# List is Mutable becasue it allows to perform Mofification,updation,and item Assignment
#=======================================================================================
a=[100,"MD",2+4j,True,5.86]
print(a,type(a),id(a))
print(a[1])
a[1]="Mohammad" # Modification
print(a,type(a),id(a))
#==============================================================================================
# IMP: It checks the element from 1 to 3 like "MD",2+4j,True and then replace it with kaif Alam
#==============================================================================================
a[1:4]=["Kaif","Alam"]
print(a,type(a),id(a))
a.insert(1,"Mohammad") # insert at index 1
print(a,type(a),id(a))
print("==" * 25)
b=[100,"kaif",3+6j]
print(b,type(b))
print(len(b))
b=[] # One way of defining empty list
print(b,type(b))
print(len(b))
b=list() # Another way of defining empty list
print(b,type(b))
# ====================
# Gives an Error
#a=list("kaif","50")
#print(a,type(a))
# ====================
a="MISSISSIPPI"
print(a,type(a))
b=list(a)
print(b,type(b))
a="ABRAKADABRA"
print(a,type(a))
b=list(a)
print(b,type(b))
print("==" * 25)
# =========================================
# Converting list into bytes and vice versa
# =========================================
lst1=[10,20,10,20,30,40,50]
print(lst1,type(lst1))
b=bytes(lst1)
print(b,type(b))
lst2=list(b)
print(lst2,type(lst2))
print("==" * 25)
# ==============================================================================================
# ALL FUNDAMENTAL VALUE AREN'T POSSIBLE TO CONVERT INTO LIST BCOZ THEY ALL ARE NON ITERABKLE OBJ
#a=15
#b=list(a)
#print(b,type(b))
#a=1.5
#b=list(a)
#print(b,type(b))
#a=True
#b=list(a)
#print(b,type(b))
#a=2+3j
#b=list(a)
#print(b,type(b))
# ==================
lst=([10])
print(lst,type(lst))
lst=([10])
b=list(lst)
print(b,type(b))
lst=([True,False])
print(lst,type(lst))
s="Mississippi"
print(s,type(s))
t=list(s) # converting str to list
print(t,type(t))
s="Mississippi"
print(s,type(s))
t=[s] # converting str to list
print(t,type(t)) # giving O/P as a Individual word
print("==" * 25)
s="Mississippi"
print(s,type(s))
t=list([s]) # gives O/P as a ['Mississippi']
print(t,type(t))
print("==" * 25)
s="Mississippi"
print(s,type(s))
t=list[s] # # gives O/P as a ['Mississippi']
print(t,type(t))  # list['Mississippi'] <class 'types.GenericAlias'>
print("==" * 25)
# ==========================
### Pre-Defined Func in list
# ==========================
lst=[10,1.67,"Mohammad",3+5j,True]
print(lst,type(lst),id(lst))
# ===============================================
# print(lst.append("Kaif")) give None as a result
# ===============================================
lst.append("Kaif")
print(lst,type(lst),id(lst))
print("==" * 25)
# ===============================================
# ---------------append(value)-------------------
# ===============================================
print("==" * 8, "listobj.append(value)","==" *8)
a=list()
print(a,type(a),id(a))
a.append(10)
a.append(20)
a.append(20.68)
a.append(True)
a.append("Mohammad")
print(a,type(a),id(a))
b=[]
print(b,type(b),id(b))
b.append(250)
b.append("Bob")
b.append(False)
b.append("@&^^")
print(b,type(b),id(b))
# ====================================================================
# NOTE: By the use of append func we can store only 1 value at a time
# listobj.append() always add value at the end of the list
# ====================================================================
print("==" * 25)
# ===============================================
# -----------insert(index,value)-----------------
# ===============================================
print("==" * 8, "insert(index,value)","==" *8)
# =====================================================================
# insert(index,value) function
# invalid positive (+ve) index add value at the end of the list
# invalid Negative (-ve) index add value at the first index of the list
# =====================================================================
a=[33,"Kaif","Branch:",67]
print(a,type(a),id(a))
# ==================================================
# print(a.insert(2,"Shaikh")) gives None as a result
# ==================================================
a.insert(2,"Shaikh")
print(a,type(a),id(a))
a.insert(4,"AIML")
a.insert(5,"Percentage:")
print(a,type(a),id(a))
a.insert(1,"Name:")
print(a,type(a),id(a))
print("==" * 25)
# ===============================================
# Invalid Index Example
# ===============================================
a=[33, 'Name:', 'Kaif', 'Shaikh', 'Branch:', 'AIML', 'Percentage:', 67]
a.insert(122,3+5j)
print(a,type(a),id(a))
a.insert(-54,100)
print(a,type(a),id(a))
print("==" * 25)
# ===============================================
# --------------listobj.remove()-----------------
# ===============================================
print("==" * 7, "listobj.remove()","==" *8)
# ==============================================================
# listobj.remove(value) removes 1st occurrence of specified val
# if val doesn't exist then get value error
# ==============================================================
lst=["Mumbai",524,"Thane",44.86,3.2+4j]
print(lst,type(lst),id(lst))
lst.remove("Thane")
print(lst,type(lst),id(lst))
lst.remove(3.2+4j)
lst.remove("Mumbai")
lst.remove(524)
lst.remove(44.86)
# =================================================================
# lst.remove(False) we will get value Error bcoz x is not in a list
# =================================================================
print(lst,type(lst),id(lst))
lst=[10,20,30,20,10,40,10,20,40,30]
print(lst,type(lst),id(lst))
lst.remove(10) # 1st Occurrence 10 will be removed
print(lst,type(lst),id(lst))
lst.remove(10)
print(lst,type(lst),id(lst))
lst.remove(30)
lst.remove(40)
# ==============================================================
#lst.remove(100) we will get value Error bcoz x is not in a list
# ==============================================================
print(lst,type(lst),id(lst))
print("==" * 25)
# ===============================================
# ------------------pop(index)-------------------
# ===============================================
print("==" * 10, "pop(index)","==" *10)
# ==================================================================
# pop(index) is used to remove the element by valid +ve or -ve index
# if we enter invalid index the we will get an Index Error
# ==================================================================
print("==" * 10, "pop(index)","==" *10)
lst=[10,20,30,10,40,10,30,50,30,20]
print(lst,type(lst),id(lst))
lst.pop(1)
print(lst,type(lst),id(lst)) # 20 is removed from the list
lst.pop(-3)
print(lst,type(lst),id(lst)) # 50 is removed from the list
# ================================================================
# lst.pop(-10) it will give an Index Error pop index out of range
# ================================================================
lst.pop(-len(lst))
lst.pop(len(lst)-1)
print(lst,type(lst),id(lst))
print("==" * 25)
# ===================================================================================
# if we try to pop from this type of list then we will get popped element as a result
# ===================================================================================
print([20,30,50].pop(1))
# =====================================================================================================
# print([].pop(1)) IndexError: pop from empty list
print(list("kaif").pop(0)) # it will remove the 0th index and get an o/p k
# print(list(20,30,50).pop(1)) TypeError: list expected at most 1 argument,single int is not iterable
# =====================================================================================================
print("==" * 25)
# ===============================================
# ---------------------pop()---------------------
# ===============================================
print("==" * 10, "pop()","==" *11)
# =========================================================================
# pop() is used to remove the last element of the list
# if we call this function in empty list [] then we will get an Index Error
# =========================================================================
lst=[33, 'Name:', 'Kaif', 'Shaikh', 'Branch:', 'AIML', 'Percentage:', 67]
print(lst,type(lst),id(lst))
lst.pop()
lst.pop()
print(lst,type(lst),id(lst))
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()
lst.pop()
print(lst,type(lst),id(lst))
print("==" * 25)
# ===============================================
# list().pop() IndexError: pop from empty list
# [].pop() IndexError: pop from empty list
# ===============================================
# ------------------clear()-------------------
# ===============================================
print("==" * 10, "clear()","==" *10)
# =========================================================================
# clear() is used to remove all elements from the list
# if we call this function in empty list [] then we will get space or None.
# =========================================================================
lst=[10,20,30,10,40,10,30,50,30,20]
print(lst,type(lst),id(lst))
print(len(lst))
lst.clear()
print(lst,type(lst),id(lst))
print(len(lst))
# ==============================================
# in below both cases we get an output as a None
# ==============================================
print([].clear())
print(list().clear())
print("==" * 25)
print("==" * 5, "del operator","==" *5)
# ===============================================
# ------------------del-------------------
# ==================================================================================
# syntax1: del listobj [index]- removes element based on indexing
# syntax2: del listobj [Begin index:End Index:Step] removes element based on slicing
# syntax1: del listobj  removes all elements + List object also
# ==================================================================================
lst=[33, 'Name:', 'Kaif', 'Shaikh', 'Branch:', 'AIML', 'Percentage:', 67]
del lst[0]
print(lst)
del lst[0::3]
print(lst)
# ====================================================================================================
del lst # deleted entire element and list object also
# print(lst) NameError: name 'lst' is not defined.
# NOTE: del operator can remove elements of MUTABLE OBJ with either indexing or slicing or entire obj
#       where del operator can't be used to remove the elements of IMMUTABLE OBJ but we can remove
#       the entire IMMUTABLE OBJ
# Once we remove the MUTALE or IMMUTABLE OBJ by using del operator
# whose memory space is collected by Garbage Collector. For Example
# ===================================================================================================
print("==" * 25)
print("==" * 4, "use of del operator on IMMUTABLE OBJ","==" *4)
s="Mississippi"
print(s,type(s))
# =========================================================================
# del s[2]   TypeError: 'str' object doesn't support item deletion
# del s[2:5]   TypeError: 'str' object doesn't support item deletion
del s # IMMUTABLE OBJ can be removed
# print(s)  NameError: name 's' is not defined
# =========================================================================
print("==" * 25)
print("==" * 4, "Finding unique elements in the list","==" *4)
lst=[10,20,30,10,40,10,30,50,30,20]
print(lst,type(lst),id(lst))
s=set(lst)
print(s,type(s),id(s)) # Gives Unique Elements from the list
print("==" * 25)
# ===============================================
# ----------------index(value)-------------------
# ===============================================
print("==" * 8, "index(value)","==" *8)
lst=[10,20,30,40,10,50,60,10,20,10]
print(lst)
print(lst.index(10))
print(lst.index(50))
# ==============================================================
# print(lst.index(100)) ValueError: list.index(x): x not in list
# ==============================================================
print("==" * 25)
# =====================================================================
# ---------------enumerate(obj)----------------------------------------
# it is used to get both index and val while iterating over a sequence
# =====================================================================
print("==" * 5, "enumerate(obj)","==" *5)
lst=[10,20,30,40,10,50,60,10,20,10]
print(lst)
for i,v in enumerate(lst):
    print(i,"---->",v)
print("==" * 25)
for i,v in enumerate(lst):
    if(v==10):
        print(i,"---->",v)
print("==" * 25)
for i, v in enumerate(lst):
    if (v == 60):
        print(i, "---->", v)
print("==" * 25)
s="Mississippi"
for i,v in enumerate(s):
    print(i,"---->",v)
print("==" * 25)
for i,v in enumerate(s):
    if (v == "s"):
        print(i,"---->",v)
print("==" * 25)
for i,v in enumerate(s):
    if (v == "i"):
        print(i,"---->",v)
print("==" * 25)
# ===============================================
# -------------copy()--shallow copy--------------
# ===============================================
print("==" * 6, "copy()--shallow copy","==" *6)
lst1=[10,30,50,"Mumbai",30.6]
print(lst1,type(lst1),id(lst1))
lst2=lst1.copy()
print(lst2,type(lst2),id(lst2)) # both obj content are same but stored at different memory address
lst1.append(40)
print(lst1,id(lst1)) # it will add the element 40 at the memory address of list 1
lst2.append("University")
print(lst2,id(lst2)) # it will add the element university at the memory address of list 2
                     # The changes are not reflecting to each other
print("==" * 25)
# ===============================================
# -------------copy()--deep copy--------------
# ===============================================
print("==" * 7, "copy()--deep copy","==" *7)
lst1=[10,30,50,"Mumbai"]
print(lst1,id(lst1))
lst2=lst1
print(lst2,id(lst2))
lst1.append("University")
lst2.insert(2,5)
print(lst1,id(lst1))
print(lst2,id(lst2)) # by adding an element on lst1 it is reflecting on lst 2 and vice versa
lst2.remove("University")
print(lst1,id(lst1))
print(lst2,id(lst2))
print("==" * 25)
# ===============================================
# ------------------copy()-----------------------
# ===============================================
print("==" * 10, "copy()","==" *10) # it is similar to shallow copy
lst1=[10,30,50,"Mumbai"]
lst2=lst1.copy()
print(lst1,id(lst1))
print(lst2,id(lst2))
lst1.remove("Mumbai") # It will remove only from the lst1 [10, 30, 50] 1451470418368
print(lst1,id(lst1))
print(lst2,id(lst2))
print("==" * 25)
# ===============================================
# -----------------count(value)------------------
# ===============================================
print("==" * 8, "count(value)","==" *8)
lst=[10,20,30,40,10,50,60,10,20,10,20,30,40,20]
print(lst)
print(lst.count(10))
print(lst.count(20))
print(lst.count(30))
print(lst.count(400)) # value does not exist then we will get 0
str="MISSISSIPPI"
print(list(str))
print(str.count("S"))
print(str.count("P"))
print(str.count("J")) # value does not exist then we will get 0
str="abrakadabra"
b=print(list(str))
print(str.count("a"))
print(list("ABRAKADABRA").count("A")) # it will give an O/P count of A is 5
print(['A', 'B', 'R', 'A', 'K', 'A', 'D', 'A', 'B', 'R', 'A'].count("A")) # it will give an O/P count of A is 5
print(["ABRAKADABRA"][0].count("B"))
print("==" * 25)
# ===============================================
print("==" * 7, "IMPORTANT QUESTION","==" *7)
# ===============================================
x=[1,2,3]
print(x,id(x))
y=x
print(id(x)== id(y))
del x
print(y,id(y))
print("==" * 25)
# ===============================================
# -------------------reverse()-------------------
# ===============================================
print("==" * 8, "reverse()","==" *8)
lst=[10.20,"Kaif",50.6,2+5j]
print(lst,id(lst))
# ==========================================================
# print(lst.reverse()) it will give an output as a None type
# ==========================================================
lst.reverse()
print(lst,id(lst))
str="MISSISSIPPI"
b=list(str)
b.reverse()
print(b,id(b))
print("==" * 25)
# ===============================================
# -------------------sort()----------------------
# ===============================================
print("==" * 9, "sort()","==" *9)
# ==============================================================================
# syntax1: lisobj.sort() ------ Gives the result in ascending order
# syntax2: lisobj.sort(reverse=False)------ Gives the result in ascending order
# syntax3: lisobj.sort(reverse=True)------ Gives the result in descending order
# data must be of similar type
# ==============================================================================
lst=[10,23,-14,60,-37,48]
print(lst,id(lst))
lst.sort()
print(lst,id(lst))
lst.sort(reverse=False) # Gives the result in ascending order
print(lst,id(lst))
lst.sort(reverse=True) # Gives the result in descending order
print(lst,id(lst))
print("==" * 25)
# ===============================================
# -------------------extend()--------------------
# ===============================================
print("==" * 9, "extend()","==" *9)
# =========================================================================
# syntax=listobj1.extend(listobj2)
#               OR
# syntax=listobj1+listobj2+.........+listobjn
# =========================================================================
lst1=["seat","Name","city"]
lst2=[33,"Kaif","Mumbai"]
print(lst1,id(lst1))
print(lst2,id(lst2))
lst1.extend(lst2) # it will merge the content in same memory address
print(lst1,id(lst1))
lst3=lst1+lst2
print(lst3,id(lst3)) # it will merge the content in diff memory address
print("==" * 25)
print("==" * 7, "Question","==" *7)
lst=[10,20,20,60,40,30,79,89]
print("Max no in list: ",max(lst))
#=============================================
# Finding Max times repeated Value in the list
#=============================================
print("==" * 7, "MAX Repeated Value","==" *7)
m=max(lst,key=lst.count)
print("Max times repeated Value: ",m)
print("==" * 25)
print("==" * 7, "INNER/NESTED LIST","==" *7)
# ===============================================
# --------------INNER/NESTED LIST----------------
# ===============================================
lst=[10,20,"AIML",[60,40,30,79],89,47,["Kaif","Mumbai","Canada"]]
for val in lst:
    print(val,"---->",type(val),"---->",type(lst))
print(lst[-1],type(lst[-1])) # indexing
print(lst[2],type(lst[2]))   # indexing
print(lst[2:7])
print(lst[0:4])
print(lst[0:7])
print(lst[-4][-2]) # Negative Indexing
lst.append(["saudi","India"]) # appending another list
print(lst)
lst[-1].insert(-1,"Nepal")
print(lst)
lst[3].sort()
print(lst)
lst[3].sort(reverse=True) # sort in descending order of index 3 element
print(lst)
print(lst[3][0::2])
lst[3].clear()
print(lst)
lst[3].append("Name")
lst[3].append("City")
print(lst)
del lst[6]
print(lst)
del lst[3]
print(lst)
lst.insert(2,["Mumbai",30,60,"Maharashtra"])
print(lst)
lst[2].append("Gmail")
print(lst)
del lst[2::4]
print(lst)
print("==" * 25)
# ===============================================
# -----------Matrix using nested list------------
# ===============================================
print("==" * 4, "matrix using nested list","==" *4)
mat1=[[9,8,7],[6,5,4],[3,2,1]]
for row in mat1:
    print(row)
mat2=[[1,2,3],[4,5,6],[7,8,9]]
for row in mat2:
    print(row)
mat3=mat1+mat2
print(mat3,type(mat3))
for row in mat3:
    print(row)
print("==" * 25)
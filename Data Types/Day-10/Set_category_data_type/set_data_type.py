# Day-10
# Topic- set category data type
# Done By - Mohammad Kaif Alam
# =======================================================================
# The purpose set cat data types is "To store multiple values of same,
# different or both types in single obj with UNIQUE elements only {}".
# ==========================================================================================================
# object of set belongs to both MUTABLE (we can do changes on same addr.) and IMMUTABLE because
# set never allows to perform an item Assignment
# on the obj of set we cannot perform indexing and slicing operation bcoz set never maintains Inertion order
# set displays any of the possibility of the elements of set
# ==========================================================================================================
print("==" * 25)
s1={10,20,30,40,20,10,30} # storing only unique values
print(s1,type(s1))
s2={10,"HTML","CSS","JavaScript","Python","HTML"}
print(s2,type(s2))
print("==" * 25)
# ===============================================
# ---------MUTABLE and IMMUTABLE property--------
# ===============================================
print("==" * 5, "MUTABLE and IMMUTABLE property","==" *5)
s1={10,"HTML","CSS","JavaScript","Python","HTML"}
# ===========================================================================
# s1[1]=30 TypeError: 'set' object does not support item assignment IMMUTABLE
# ===========================================================================
print(s1,type(s1),id(s1))
s1.add("SQL")
# ===========================================================================
# The element will be added at same memory address thats why it is MUTABLE
# ===========================================================================
print(s1,type(s1),id(s1))
print("==" * 25)
# ===============================================
# ------------Empty and Non Empty Set------------
# ===============================================
print("==" * 5, "Empty and Non Empty Set","==" *5)
s=set()
print(s,type(s))
print(len(s))
s1={10,20,30,40,20,10,30}
print(s1,type(s1))
print(len(s1))
print("==" * 25)
# ===============================================================
# ----------To find the unique elements from list or str---------
# ===============================================================
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
# =================================================
# ----------Pre-Defined Functions in set()---------
# =================================================
print("==" * 5, "Pre-Defined Functions in set()","==" *5)
# =================================
# ------------1-add()-------------
# =================================
print("==" * 8, "1-add()","==" *8)
s=set()
print(s,type(s),id(s))
s.add(10)
s.add(34.56)
s.add("mumbai")
s.add("Python")
print(s,type(s),id(s))
# =========================================================================
# Elements will be added random bcoz set never maintains an insertion order
# =========================================================================
s1={'Python', 10, 34.56, 'mumbai'}
print(s1,type(s1),id(s1))
s1.add("Imteyaz")
print(s1,type(s1),id(s1)) # Elements will be added at same memory address thats's why Mutable
print("==" * 25)
# ========================================
# ------------2-remove(value)-------------
# ========================================
print("==" * 8, "2-remove(value)","==" *8)
s1={10,20,30,40,20,10,30}
print(s1,type(s1)) # print only Unique Values
s1.remove(20)
print(s1,type(s1))
# ============================================================================================
# s1.remove("Imteyaz") KeyError: 'Imteyaz' we are trying to remove those element which are not
# present in set.
# ===============
s1.remove(10)
s1.remove(30)
s1.remove(40)
print(s1,type(s1)) # set becomes empty
# ============================================
# s1.remove(40) KeyError: 40 bcoz set is empty
# ============================================
print("==" * 25)
# ========================================
# ------------3-discard(value)------------
# ========================================
print("==" * 8, "3-discard(value)","==" *8)
s={10, 'Python', 34.56, 'mumbai'}
print(s,type(s))
s.discard("Python")
print(s,type(s))
# IMPORTANT==================================================================
s.discard("Imteyaz") # No Error will come the o/p display shows no error
# s.remove("Imteyaz") KeyError: 'Imteyaz'
set().discard("Imteyaz") # No Error will come the o/p display shows no error
# set().remove("Imteyaz")  KeyError: 'Imteyaz'
# ===========================================================================
print("==" * 25)
# ================================
# ------------4-pop()-------------
# ================================
print("==" * 8, "4-pop()","==" *8)
s1={10,20,30,40}
# =============================================================================================
# This func is used for removing any ARBITARY ELEMENT frm set obj provided NO ORDER OF DISPLAY
# =============================================================================================
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
# =================================================
# print(s1.pop()) KeyError: 'pop from an empty set'
# set().pop() KeyError: 'pop from an empty set'
# =================================================
print("==" * 25)
# ====================================
# -------------5-clear()--------------
# ====================================
print("==" * 8, "5-clear()","==" *8)
s1={10,20,30,40}
print(s1,type(s1))
s1.clear()
print(len(s1)) # Gives 0 set becomes empty due to s1.clear()
print(s1,type(s1))
print(s1.clear())
print("==" * 25)
# =======================================
# -----------6-isdisjoint()--------------
# =======================================
print("==" * 8, "6-isdisjoint()","==" *8)
# ===================================================================================================
# This gives TRUE if there is no common element else if there is one common element then gives False
# ===================================================================================================
s1={10,20,30,40}
s2={50,60,70}
s3={10,80,90}
print(s1.isdisjoint(s2)) # gives True bcoz there is no common element
print(s1.isdisjoint(s3)) # gives False bcoz 10 is common no in set 1 and set3
print(s2.isdisjoint(s3)) # gives True bcoz there is no common element
s1=set()
s2=set()
print(s1.isdisjoint(s2)) # gives True on empty set
print(set().isdisjoint(set())) # gives True on empty set
print(set().isdisjoint({10,20,30,40})) # It also gives true as an O/P
print("==" * 25)
# ========================================
# -------------7-issuperset()-------------
# ========================================
print("==" * 8, "7-issuperset()","==" *8)
# ======================================================================
# This func returns TRUE if setobj1 contains all the elements of setobj2
# ======================================================================
s1={10,20,30,40}
s2={30,40}
s3={70,80,10}
print(s1.issuperset(s2)) # Gives TRUE bcoz set1 contains all the elements of set2
print(s1.issuperset(s3)) # Gives FALSE bcoz set1 does not contain all the elements of set3
print(set().issuperset(set()))  # Gives TRUE
print("==" * 25)
# ========================================
# --------------8-issubset()--------------
# ========================================
print("==" * 8, "8-issubset()","==" *8)
# ===========================================================================
# This func returns TRUE if all the elements of setobj1 is present in setobj2
# ===========================================================================
s1={10,20,30,40}
s2={10,20,30,40,50,60}
print(s1.issubset(s2)) # Gives TRUE bcoz all the elements of s1 is present in s2
print(s2.issubset(s1)) # Gives FALSE as an O/P
print(set().issubset({10,20,50,60})) # Gives TRUE as an O/P
print(set().issubset(set())) # Gives TRUE as an O/P
print({10,20,50,60}.issubset(set())) # Gives FALSE as an O/P
print("==" * 25)
# ========================================
# ---------------9-union()----------------
# ========================================
print("==" * 8, "9-union()","==" *8)
# ========================================================================================
# This Func is used for obtaining Unique values of setobj1 and setobj2 & place in setobj3
# ========================================================================================
s1={10,20,30,40}
s2={10,20,60,70}
s3=s1.union(s2)
print(s3) # {70, 40, 10, 20, 60, 30} gives Unique elemennts from both sets rendomly.
print(s1.union(s2)) # {70, 40, 10, 20, 60, 30} gives Unique elemennts from both sets rendomly
s1={"C","JAVA","PYTHON"}
s2={"HTML","JAVA","PYTHON","CSS"}
s3=s1.union(s2)
print(s3) # {'CSS', 'HTML', 'JAVA', 'C', 'PYTHON'} gives Unique elemennts from both sets rendomly.
print("==" * 25)
# ==========================================
# ------------10-intersection()-------------
# ==========================================
print("==" * 8, "10-intersection()","==" *8)
# ================================================================
# This Func is used for obtaining Common elements from both setobj
# ================================================================
s1={10,20,30,40}
s2={10,60,70,20}
s3=s1.intersection(s2)
print(s3) # {10, 20} gives as an O/P these two elements are common
s1={"C","JAVA","PYTHON"}
s2={"HTML","JAVASCRIPT","DJANGO","CSS"}
s3=s1.intersection(s2)
# =========================================================================
# IMP- IF NO COMMON ELEMENT IS PRESENT THEN IT WILL RETURN EMPTY SET set()
# =========================================================================
print(s3) # set() gives empty set bcoz there is no common element is present
# ==========================================
# --------------IMP Question----------------
# ==========================================
print("==" * 8, "IMP Question","==" *8)
s1={10,20,30,40}
s2={10,60,70,20}
s3={1,2,"python"}
print(s1,s2,s3,sep="\n")
print("s1.intersection(s2,s3)")
s4=s1.intersection(s2,s3) # it will give an EMPTY set()
print(s4) # because s1 intersection with s2 give {20,10} but s2 intersection with s3 it will give empty set
print("==" * 25)
# ==========================================
# ------------11-difference()---------------
# ==========================================
print("==" * 8, "11-difference()","==" *8)
# ==============================================================
# This Func removes Common elements from both set and takes
# remaining elements from both sets and place them in a new set.
# ==============================================================
s1={10,20,30,40}
s2={10,60,70,20,70,90}
s3=s1.difference(s2) # returns the elements present in the set s1 but not in the set s2
print(s3)
s3=s2.difference(s1) # returns the elements present in the set s2 but not in the set s1
print(s3)
x={"python","HTML","CSS"}
y={"JAVASCRIPT","DJANGO","NUMPY"}
z=x.difference(y)
print(z)
z=y.difference(x)
print(z)
s1={10,20,30,40}
s2={10,20,30,40}
s3=s1.difference(s2) # gives an o/p as Empty set set()
print(s3)
print("==" * 25)
# ====================================================
# ------------12-symmetric_difference()---------------
# ====================================================
print("==" * 7, "12-symmetric_difference()","==" *7)
# ==================================================================================================================
# This Func removes the common element and takes remaining elements from both sets and place them in other variable
# setobj1.symmetric_difference(setobj2)
# setobj1.union(setobj2).difference(setobj1.intersection(setobj2))
# ==================================================================================================================
a={10,20,30,78,68}
b={50,70,90,10,80,20,40}
c=a.symmetric_difference(b) # gives combined result except common elements such as 10,20
print(c)
s1={10,20,30,40}
s2={10,20,30,40}
s3=s1.symmetric_difference(s2) # gives an o/p as Empty set set()
print(s3)
s1={10,20,30,40,52,55}
s2={10,40,50,90,10,70}
s3=s1.union(s2).difference(s1.intersection(s2))
print(s3)
print("==" * 25)
# ======================================
# ------------13-update()---------------
# ======================================
print("==" * 8, "13-update()","==" *8)
# =========================================================================================
# This Func is used for adding or merging of setobj2 with setobj1 and store them in setobj1
# =========================================================================================
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
# ===========================================================
# ------------14-symmetric_difference_update()---------------
# ===========================================================
print("==" * 5, "14-symmetric_difference_update()","==" *5)
# =========================================================================================
# This Func removes the common elements from both set and takes remaining elements from
# both sets and place them in set1 itself
# =========================================================================================
s1={10,20,30,40}
s2={10,20,35,45}
s1.symmetric_difference_update(s2)
print(s1)
# =======================================
# ------------del operator---------------
# =======================================
v={1,2,3,4,5,6,7,9}
print(v)
# ==================================================================
# del v[2:4] TypeError: 'set' object does not support item deletion
# ==================================================================
del v # it is possible it will delete overall set object v
# print(v)  NameError: name 'v' is not defined The execution will stop here rest of the commands
# will not be executing bcoz it tries to access something thst has been deleted python stops at exact line
print("==" * 25)
# =======================================
# ------------IMP Question---------------
# =======================================
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
# ============================================
# ------------Nested/INNER sets---------------
# ============================================
print("==" * 8, "Nested/INNER sets","==" *8)
# ==========================================================================================
# case1: It is not possible to define one set in another set bcoz sets are unhashable type
# (Not Possible indexing and slicing)
# s1={"Rohit","Kohli","Dhoni",{"Messi","Ronaldo","Dhoni"}}
# print(s) TypeError: cannot use 'set' as a set element (unhashable type: 'set')
# case2: It is not possible to define one List in another set bcoz sets are unhashable type
# (Not Possible indexing and slicing)
# s2={"Rohit","Kohli","Dhoni",["Messi","Ronaldo","Dhoni"]}
# print(s) TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# case3: It is possible to define one tuple in another set bcoz tuples are IMMUTABLE
# ===========================================================================================
s3={"Rohit","Kohli","Dhoni",(10,20,"Kaif")}
print(s3)
for val in s3:
    print(val,type(val))
# ==============================================================================================
# case4: It is possible to define one set in another List bcoz List are MUTABLE and allows us to
# locate set objects by using indices.
# ====================================
s4=["Rohit","Kohli","Dhoni",{10,20,"Kaif"}]
print(s4)
print(s4[3],type(s4[3]))
s4[3].add(2+5j)
print(s4)
# ==============================================================================================
# case5: It is possible to define one set in another tuple bcoz tuples are IMMUTABLE and allows
# locate set objects by using indices.
# ====================================
s5=("Rohit","Kohli","Dhoni",{10,20,"Kaif"})
print(s5,type(s5))
print(s5[3],type(s5[3]))
s5[-1].add(50)
print(s5)
s5[-1].remove("Kaif")
print(s5)
print("==" * 25)
# ===============================================
print("==" * 7, "IMPORTANT QUESTION","==" *7)
# ===============================================
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
print("==" * 25)
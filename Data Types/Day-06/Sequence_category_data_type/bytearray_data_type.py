# Day-06
# Topic- bytearray data type
# Done By - Mohammad Kaif Alam
#==============================================================
# The purpose of bytes and bytearray is same
# "To Implement End-t0-End encryption in network based Apps".
#==============================================================
# The fuctionality is also similar but the obj of bytes belongs
# to IMMUTABLE bcoz bytes does not support Item assignment.
# whereas an obj of bytearray belongs to MUTABLE bcoz an obj of
# bytearray allows us to perform an Item Assignment.
#==============================================================
# lst=[100,-200,50,256,76,84]
# ba=bytearray(lst)
# print(ba)  ValueError: byte must be in range(0, 256)
print("==" * 25)
tpl=0,100,255,56,88,99
print(tpl,type(tpl))
ba=bytearray(tpl)
print(ba)
for val in tpl:
    print(val)
print()
print("==" * 25)
#=======================================================================
# tpl[0]=55
# print(tpl)  TypeError: 'tuple' object does not support item assignment
#=======================================================================
lst=[0,100,255,56,88,99]
print(lst,type(lst))
by=bytearray(lst)
print(by)
for val in by:
    print(val,end=" ")
#===================================================
# bytearray allows us to perform an Item Assignment
#===================================================
by[1]=78
print(by)
for val in by:
    print(val,end=" ")
print()
for val in by[::-1]: # It will reverse the value
    print(val,end=" ")
print()
print("==" * 25)
lst=[0,100,255,56,88,99]
print(lst,type(lst),id(lst))
ba=bytearray(lst)
#=====================================================================================
# It is MUTABLE bcoz it allows us to perform an item Assignment at same Memory address
#=====================================================================================
print(ba,id(ba))
for val in ba:
    print(val,end=" ")
for val in ba:
    print(val,end=" ")
print()
ba[0]=254
print(ba,id(ba))
for val in ba:
    print(val,end=" ")
print()
print("==" * 25)

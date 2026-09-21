# Day-05
# Topic- Number System Conversion
# Done By - Mohammad Kaif Alam
#==========================================================
# The Purpose of bytes data type is to
# "Implement end-to-end encryption in Network-based Apps."
# It organizes the numerical integer in the range (0,256)
#==========================================================
print("==" * 25)
lst=[100,35,200,56,0]
print(lst)
by=bytes(lst)
print(by,type(by))
print("==" * 25)
#==========================================================
#tpl=25,76,84,455,-290
#by=bytes(tpl) ValueError: bytes must be in range(0, 256)
#==========================================================
tpl=100,35,200,56,0,255,45
print(lst,type(tpl))
by=bytes(tpl)
print(by,type(by))
for val in by:
    print(val,end=" ")
print()
for val in by[::-1]:
    print(val,end=" ")
print()
print("==" * 25)
#==========================================================
# Doing INDEXING and SLICING on bytes data
#==========================================================
print(by[0])
print(by[1:5])
for val in by[1:5]:
    print(val)
print()
#==================================================================
#by[0]=2 TypeError: 'bytes' object does not support item assignment
#==================================================================

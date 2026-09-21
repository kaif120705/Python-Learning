# Day-07
# Topic- range data type
# Done By - Mohammad Kaif Alam
#==========================================================
# The Purpose of range data type is to "Maintain sequence of
# of integer values by maintaining equal interval of value.
#==========================================================
print("==" * 25)
print("==" * 6, "syntax 1 : range(val)","==" *7)
#==========================================================
# syntax 1 : range(val) generates nos from 0 upto (val-1)
#==========================================================
r=range(10)
print(r,type(r))
for val in r:
    print(val,end=" ")
print()
print("==" * 25)
#==================================================================
# syntax 2 : range(start,stop) generates nos from start to (stop-1)
#==================================================================
print("==" * 5, "syntax 2 : range(start,stop)","==" *5)
r=range(10,20)
print(r,type(r))
for val in r:
    print(val,end=" ")
print()
print("==" * 25)
#==================================================================
# NOTE : The above two syntaxes by default uses +1 step
#==================================================================
# syntax 3 : range(start,stop,step) generates nos from start to stop
#            by maintaining equal interval of value (step).
print("==" * 4, "syntax 3 : range(start,stop,step)","==" *4)
r=range(10,20,2)
print(r,type(r))
for val in r:
    print(val,end=" ")
print()
for val in range(100,111,2):
    print(val,end=" ")
print()
print("==" * 25)
# To print the certain range of values
for i in range(0,11): # val of 0 to 10
    print(i,end=" ")
print()
for val in range(10,21): # val of 10 to 20
    print(val,end=" ")
print()
for val in range(10,51,5): # val of 10 to 50 with diff of 5
    print(val,end=" ")
print()
for i in range(-9,0): # val of -9 to -1
    print(i,end=" ")
print()
for c in range(-50,-9,10): # val of -50 to -10 with the diff of 10
    print(c,end=" ")
print()
for i in range(-1,-10,-1): # val of -1 to -9 with the diff of -1
    print(i,end=" ")
print()
for i in range(-100,-201,-20): # val of -100 to -200 with the diff of -20
    print(i,end=" ")
print()
for i in range(-5,6,1): # val of -5 to 5 with the diff of 1
    print(i,end=" ")
print()
for i in range(1000,1051,10): # val of 1000 to 1050 with the diff of 10
    print(i,end=" ")
print()
r=range(1000,1041,10)
print(r[2:4])
for v in r[2:4]: # val of 1020 to 1030 with the diff of 10
    print(v,end=" ")
print()
print("==" * 25)

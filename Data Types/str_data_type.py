# Day-03
# Topic- Number System Conversion
# Done By - Mohammad Kaif Alam
#================================================
# Program 1: Exploring Single Line String Data
#================================================
print("==" * 25)
name="This is Single Line String DataType of String 123@#25"
print(name,type(name))
a=26
print(a,type(a))
a="26"
print(a,type(a))
#================================================
# Program 2: Exploring Multi Line String Data
#================================================
print("==" * 25)
python_dev="""Python Guiddo Van Rossum
flat no:207
Location:Netherlands"""
print(python_dev)
#================================================
# Program 3: Concatenation 0f str Data
#================================================
print("==" * 25)
name="Mohammad "+"Kaif "+"Alam"
print(name)
print("Python\n"*3)
no="10"+"20"
print(no)
print("==" * 25)
#=========================================================
# Program 4: int and str data type cant't be concateneted
#=========================================================
#no=10+"20"#
#print(no)# Gives an Error of int and str
name="Mohammad Kaif Alam"
University="Mumbai University"
Course="Python"
print("Name:",name)
print("Universiy:",University)
print("Course:",Course)
#=========================================================
# Program 4: Memory Management of str Data Type
#=========================================================
print("==" * 25)
name="Mohammad"
print(len(name))
print(name[0])
print(name[len(name)-1])
print(name[-len(name)])
print(name[-1])
print("==" * 25)
#=========================================================
# Program 5: Positive Indexing of str Data type
#=========================================================
s="Mohammad Kaif Alam"
print(len(s))
print(s[0])
print(s[7])
print(s[9])
print(s[17])
#=========================================================
# Program 6: Negative Indexing of str Data type
#=========================================================
print(len(s))
print(s[-1])
print(s[-len(s)])
print(s[-6])
print(len("Artificial Intelligence"))
print("python"[-1])
#=========================================================
# Program 7: Examples on Indexing of str Data type
#=========================================================
print("==" * 25)
n="Mohammad"
print(n,type(n))
print(len(n))
print(n[0])
print(n[len(n)-1])
print(n[-len(n)])
print(n[-1])
print(n[-2])
#=========================================================
# Program 8: Examples on Slicing of str Data type
#=========================================================
print("==" * 25)
n="Himalaya"
print(n,type(n))
#=================================================================
# SYNTAX 1: Syntax 1 of Slicing operation gives whole str as a O/P
#=================================================================
print(n[:])
#=================================================================
# SYNTAX 2: [start:Stop] gives a portion of the str
#=================================================================
print(n[0:5])
print(n[5:])
print(n[-5:])
print(n[2:4])
# Nothing will bw Printed
print(n[0:-8])
#=================================================================
# SYNTAX 3: [START:] starts from the START and goes till the END
#=================================================================
print(n[-8:])
#=================================================================
# SYNTAX 4: [:END] starts from BEGINING and goes up to (END-1)
#=================================================================
print(n[:-1])
print(n[0:120])
print(n[120:])
print(n[-3:8])
print(n[7:-5])
print(n[-87:122])
#=================================================================
# SYNTAX 5: [BEGIN:END:STEP] Select characters with a specified gap
# Begin = starting index : End = stopping Index (Excluded)
# Step = How many positions to move
#=================================================================
s="Netherlands"
print(s,type(s))
print(s[0:12:1])
print(s[0:12:2])
print(s[::1])
print(s[::2])
print(s[::-1])
print(s[6:11:1])
print(s[-11::1])

print(s[-5:4:-1])
# Give Space as a Result
print(s[-5:4:1])
print("==" * 25)
s="python"
print(s[-2::-2])
s="Artificial"
print(s[3:9:2])
# Gives result as a space
s="python"
print(s[2:2])
print("==" * 25)
s="python"
print(s[::-3])
print(s[5:0:-2])
print("==" * 25)
#=================================================================
# Program 8: WAP to check whether String is PALINDROME or not
#=================================================================
s="python"
print(s[::-1])
s="madam"
if s==s[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")
print("==" * 25)
#if we take Racecar 1st letter cap then it will give not a palindrome
ch="racecar"
if ch==ch[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")
print("==" * 25)
ch="Racecar"
if ch==ch[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")
print("==" * 25)
#same for word like Mom dad wow
ch="racecar"
print(ch==ch[::-1])
print("==" * 25)

a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
print("==" * 25)
print("\t\t\t Value of a is:",a)
print("\t\t\t Value of b is:{} ".format(b))
print("==" * 25)
s=a+b
sb=a-b
m=a*b
d=a/b
fd=a//b
mo=a%b
po=a**b
print("==" * 25)
print("\t\t\t  Sum of {} and {} is : {} ".format(a,b,s))
print("\t\t\t  Subtraction of {} and {} is : {} ".format(a,b,sb))
print("\t\t\t  Multiplication of {} and {} is : {} ".format(a,b,m))
print("\t\t\t  Division of {} and {} is : {} ".format(a,b,d))
print("\t\t\t  Floor Division of {} and {} is : {} ".format(a,b,fd))
print("\t\t\t  Modulo of {} and {} is : {} ".format(a,b,mo))
print("\t\t\t  pow of {} and {} is : {} ".format(a,b,po))
print("==" * 25)
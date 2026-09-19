# Conversion of int to other Possible type Value
print("==" * 25)
n=25.2
print(int(n))
a=True
b=False
print(int(a),int(b))
# converting complex into int type is not Possible
#a=5+4j
#print(int(a))
print("==" * 25)
# Converting Str int data to int is possible else not possible in any other data type
a="1234"
print(int(a))
#a="26.78"
#print(int(a))
#f="True"
#print(int(f))
#a=5+4j
#print(int(a))
#a=("kaif")
#print(int(a))
print("==" * 25)
# float()
a=25
print(float(a))
a=0
print(float(a))
a=True
print(float(a))
a=False
print(float(a))
#a=2+6j
#print(int(a)
print("==" * 25)
# Conversion of float into another data type
a="12"
print(float(a))
#f="True"
#print(float(f))
#a=5+4j
#print(float(a))
#a=("kaif")
#print(float(a))
print("==" * 25)
# Conversion of float into another data type
# ALL NON-ZERO VALUES ARE TREATED AS TRUE
# ALL ZERO VALUES ARE TREATED AS False
a=25
print(bool(a))
a=0
print(bool(a))
a=2.5
print(bool(a))
a=0.0
print(bool(a))
a=0.0000000000000000000000000000052
print(a,type(a))
print(bool(a))
a=5+4j
print(a,type(a))
print(bool(a))
a="23"
print(a,type(a))
print(bool(a))
a="2.6"
print(a,type(a))
print(bool(a))
a="True"
print(a,type(a))
print(bool(a))
# IMP Point Converting Str "False" into bool gives TRUE as a result
a="False"
print(a,type(a))
print(bool(a))
print("==" * 25)
a=2+7j
print(a,type(a))
print(bool(a))
a=0j
print(a,type(a))
print(bool(a))
a=0+7j
print(a,type(a))
print(bool(a))
print("==" * 25)
#Conversion of Pure Str of other Data Type to bool Type
a="25"
print(a,type(a))
print(bool(a))
a="24.3"
print(a,type(a))
print(bool(a))
a="False"
print(a,type(a))
print(bool(a))
a="python"
print(a,type(a))
print(bool(a))
# IMP if there is Space in Str then gives TRUE else False
a=" "
print(a,bool(a))
a=""
print(a,bool(a))
print("==" * 25)
#Conversion of Other Data Type into Possible Complex Type
a=10
print(a,type(a))
print(complex(a))
a=15.6
print(a,type(a))
print(complex(a))
a=True
print(complex(a))
#############################
a=False
print(complex(a))
#############################
print("==" * 25)
# Imp in case of taking only Imag. part as a literal then it is not returning Real Part
a=0j
print(a,type(a))
print(complex(a))
a=5j
print(a,type(a))
print(complex(a))
print("==" * 25)
a="10"
print(a,type(a))
print(complex(a))
a="1.5"
print(a,type(a))
print(complex(a))
print("==" * 25)
# Not Possible to convert bool to complex
#a="True"
#print(a,type(a))
#print(complex(a))
print("==" * 25)
a=2.3+4.3j
print(a,type(a))
print(complex(a))
#Not Possible
#a=2+4i
#print(a,type(a))
#print(complex(a))
# Converting str data into Complex data type is not Possible
#a="Python"
#print(a,type(a))
#print(complex(a))
print("==" * 25)
a=120
print(a,type(a))
b=str(a)
print(b,type(b))
a=2.5
print(a,type(a))
b=str(a)
print(b,type(b))
a=True
print(a,type(a))
b=str(a)
print(b,type(b))
a=5+4j
print(a,type(a))
b=str(a)
print(b,type(b))








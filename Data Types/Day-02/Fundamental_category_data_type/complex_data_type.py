# ================================================
# Program 1: Exploring Complex Data Type
# ================================================
c_no=2+5j
print(c_no,type(c_no))
c_no=2-5j
print(c_no,type(c_no))
c_no=-2-5j
print(c_no,type(c_no))
c_no=2.2-5.7j
print(c_no,type(c_no))
#================================================
# Program 2: Separating real and imag part
#================================================
print("==" * 25)
c_no=2.2-5.7j
print(c_no.real)
print(c_no.imag)
a=-5j
print(a.real,type(a.real))
print(a.imag,type(a.imag))
c_no=2+5j
print(c_no.real,type(c_no.real))
print(c_no.imag,type(c_no.imag))
#================================================
# Program 3: Operation on Complex Number
#================================================
print("==" * 25)
a=5+4j
b=7+9j
print(a+b)
print(a*b)
print(a/b)
#================================================
# Program 4: Complex Number Analyzer
#================================================
print("==" * 25)
C_no=7+9j
print("Complex No:",C_no)
print("Real Part",C_no.real,type(C_no.real))
print("Imaginary Part",C_no.imag,type(C_no.imag))
print("Data Type:",type(C_no))




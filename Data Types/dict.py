d1={1:"Kaif",2:"Imteyaz",3:"Hassan"}
print(d1,type(d1))
print(len(d1))
d2={"Apple":1,"Mango":3,2:"Banana",4:"Pineapple"}
print(d2,type(d2))
print(len(d2))
d3={10:2,20:3,30:4,10:50,10:0}
print(d3) # if key:val is repeated continuously then it will give last repeated val as a result
d2={1:"Apple",2:"Mango",3:"Banana",4:"Pineapple"}
print(d2,type(d2))
print(d2[1])
print(d2[2])
print(d2[3])

# print(d2[0]) KeyError: 0
# print(d2[10]) KeyError: 10
d2[5]="Orange"
print(d2)
d2[1]="Dates"
print(d2)
print("==" * 25)
d3={}
print(d3,type(d3))
d3[1]="Kaif"
d3[2]=300
d3["City"]="Mumbai"
print(d3,type(d3))
d3[1]="200"
print(d3,type(d3))
print("==" * 25)
print("==" * 7, "Pre-Defined Func in dict","==" *7)
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)
d1.clear()
print(d1)
d1={}
d1.clear()
print(d1.clear()) # when we apply this clear() on empty dict then we get None as a result
print({}.clear())
print(dict().clear())
print("==" * 25)
print("==" * 7, "pop(key)","==" *7)
# This Function is used for removing (key,val) from non-empty dict obj
# if the value of key does not exist then we will get keyERROR
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)
d1.pop(1)
print(d1)
# d1.pop(100)  KeyError: 100
# print({}.pop(1)) KeyError: 1
# print(dict().pop(3)) KeyError: 3
print("==" * 25)
print("==" * 7, "popitem()","==" *7)
# This Func is used for removing last (key:value) from Non-Empty dict obj
# when we call this func on empty dict  then we will get keyERROR
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)
d1.popitem()
print(d1)
d1.popitem()
print(d1)
# print({}.popitem()) KeyError: 'popitem(): dictionary is empty'
# print(dict().popitem()) KeyError: 'popitem(): dictionary is empty'
print("==" * 25)
print("==" * 7, "copy()","==" *7)
# This func is used for copying the content of one obj into another dict obj
# Implementation of shallow copy
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1,id(d1))
d2=d1.copy()
print(d2,id(d2))
d1[6]="Kiwi"
print(d1,id(d1))
d2[1]="Apple"
print(d2,id(d2))
print("==" * 25)
print("==" * 7, "M-IMP get(key)","==" *7)
# This Func is used for obtaining val of val by passing the val of key
# if the val of key does not exist then we get NONE as a result but
# In case of dictobj[key] alternate method we will be getting KeyError
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)
print(d1.get(3))
a=d1.get(5)
print(a)
print(d1.get(10))
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)
print(d1[1])
# print(d1[8])  KeyError: 8
print("==" * 25)
print("==" * 7, "keys()","==" *7)
d1={1: 'Dates', 2: 'Mango', 3: 'Banana', 4: 'Pineapple', 5: 'Orange'}
print(d1)



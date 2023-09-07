#print("sipder", "man", sep = "-")

número=2
número+=4 # esto es = número + 3
print(número)

a="Dani" 
b=3 
c=3.25
d=21.25j
print(type(a)) #<class 'str'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'float'>
print(type(d)) #<class 'complex'>

y=2.2548965785214
dos_decimales=round(y,2)
cuatro_decimales=round(y,4)
print(dos_decimales)
print(cuatro_decimales)

d="2" 
e="2.25" 
print(type(d)) #<class 'str'>
print(type(e))#<class 'str'>
print(type(int(d))) #<class 'int'>
print(type(float(d)))#<class 'float'>

t=pow(4,3) # 4 elevado a 3 (64)
print(t)

t=(4**3) # 4 elevado a 3 (64)
print(t)

a=abs(4)
b=abs(-25) #valor absoluto
print(a)
print(b)

x=divmod(244,5) #Devuelve el cociente (48) y el resto (4)
print(x)

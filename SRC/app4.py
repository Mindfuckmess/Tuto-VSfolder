print (5+15)
print (5-1)
print (5*15)
print (1/5)
print (5**15)
print (10%3) #módulo (caben 3 veces 3 en 10 y sobra 1. Ese 1 es el módulo)
x=divmod(10,3) #asi podemos verlo tambien. DEvuelve 3 (veces 3) y 1 que es el resto/módulo
print(x)

#INDICADORES DE COMPARACIÓN
n1=10
n2=15
print(n1<n2) #true
print(n1>n2) #false
print(n1<=n2) #true
print(n1>=n2) #false
print(n2==15) #true

#DATOS DEL USUARIO
resultado=int(input("Ingresa tu edad:")) #pongo int para que lo convierta en integer. Sino lo entiende como string
print(resultado)
if (resultado<=38): #OJO PON LOS DOS PUNTOS
    print ("Dani eres un campeón")
else: #OJO PON LOS DOS PUNTOS
    print ("Dani eres un viejoven")
#str(22) OJO meto un int
#float("22,5")  OJO meto un str
#bool ("")  OJO. Casi todos los que metamos van a ser true salvo(false, 0, un string vacio"" o none) o poner not (ejemplo)
print (bool(not "2"))
d=22
print (d<30 and d>10)
print (d<20 or d>23) #las dos son mentira (FALSE)
print (d<30 or d>23) #una de las dos es verdad (TRUE)

h="""hola caracola, 
esta noche coca cola""" #triple comilla ("" o '') para que reconozca varias lineas de un str y las imprima por separado
print (h)
h='''si te mola en rock and rola, 
ponte un disco en la gramola''' #triple comilla ("" o '') para que reconozca varias lineas de un str y las imprima por separado
print (h)
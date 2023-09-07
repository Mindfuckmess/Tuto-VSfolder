print ("hola mundo")
#Esto es un comentario que no vale para nada
#y esto es para demostrar que puedo poner varias líneas de comentarios
#Si quiero poner varias líneas en una sola, hay que separar ordenes por ;
x = 5; y = 4; sum = x + y; print(sum)
name = "Dani" 
surname = "Urbina"
print(name, surname)
print("Hoy hacemos un", "6" ,sum)
Frutas= ("orange", "mango", "plátano")
print(Frutas) #y así hago la lista de la compra
if 5 > 4:
    x = "Su Puta Madre"
    print (x.upper())#UPPER para mayusculas y LOWER para minusculas
print ("el bloque termina aquí")
#Las VV solo pueden empezar por número, letra o _
#Las VV solo pueden contener número, letra o _
#Nombre es un String (texto) Los String siempre entre comillas
_Nombre = "Juan"
#Age es un Int/Integer (Número entero) Va sin comillas.
#Si le pones comillas el texto se trata como un string
Age = 21
print(_Nombre, Age)
#Para variables largas, separa con _ (no con espacios)
Cumpleaños_de_Dani = "11 de junio"
print (Cumpleaños_de_Dani.lower())
#También puedes usar Mayúsculas en ves de espacios
CumpleanosDeCamelia = "14 de abril"
print (CumpleanosDeCamelia)
#Peso es un Float (Números con decimales)
Peso = 108.7
print (Peso)
#Usar comillas simples si el string incluye "" (o vicebersa)
frase = 'Te he dicho que "Python es divertido de aprender"'
print (frase)
#Lo Booleanos son VV que expresan su valor en términos de TRUE o FALSE
#Se imprime si la condición que se ha puesto es verdadera o falsa.
print(5<6) #True 
print(5>6) #False
suma = Age + Peso #para definir funciones y VV no han falta parentesis ni "" 
print (suma)
print (frase.find ("Python")) #Busca la posición del texto en un string
print (frase.replace("Python", "R")) #Reemplaza un string por otro
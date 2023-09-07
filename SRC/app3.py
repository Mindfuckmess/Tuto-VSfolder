age=18
if (age>=0) and (age<=10):
    print ("peque")
elif (age>=11) and (age<=17):
    print ("mediano")
else:
    print ("mayorcito")

print (not 1==1) #not TRUE=FALSE
print (not 1!=1) #not FALSE=TRUE

a=1.11548625896258
x=round(a,2)
z="Al final, "
y="gano la ".replace ("gano", "pierdo") # OJO mira que has usado la función.replace al definit la variable
s= "cabeza"
if (x==1,11):    
    print(z + "si me tomo una cerveza " + y + s)
d="me entra tos"
  #0123456789
s= "pero si me tomo 3, "
if (x<=2):
    print ("y si me tomo dos " + d) 
if (x<=4):
    print (s + "me agacho y no me ves")
print (not "tos" in d) #IN devuelve un boobleano TRUE/FALSE
print (d.find("tos")) #IN devuelve el índice en el que se encuentra la palabra dentro de la VV
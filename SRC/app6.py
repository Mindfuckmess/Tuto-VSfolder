W= ["Norte", "Sur", "Este", "Oeste"] #[] para hacer una lista
print (W[0]) #Norte
print (W[2]) #Este
print (W[-1]) #Oeste
print (W[-3]) #Sur
print (W[1:3]) # ['Sur', 'Este']
print (W[:2]) # ['Norte', 'Sur']

W= ["Norte", "Sur", "Este", "Oeste"] 
W.pop()
print (W)

W.remove("Sur")
print (W)

W.insert(2,"Oeste")
print (W)

W.append("Sur")
print (W)
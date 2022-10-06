puntoA=0
puntoB=0

puntoA=(int)(input("¿En qué punto es la primera misión? (punto más cercano a 0)= "))
puntoB=(int)(input("¿En qué punto es la segunda misión? (punto más lejano a 0)= "))

if(puntoA<0 and puntoB<0):
    print("La distancia recorrida es: ",abs(puntoB),)

if(puntoA>0 and puntoB>0):
    print("La distancia recorrida es: ",puntoB,)
    
if(puntoA<0 and puntoB>0):
    print("La distancia recorrida es: ",abs(puntoA)*2+puntoB,)
if(puntoA>0 and puntoB<0):
    print("La distancia recorrida es: ",puntoA*2+abs(puntoB),)
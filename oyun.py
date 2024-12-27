x=2
while x>3:
  print("Richtig")
  x-=1
print("ende")
#geheime Zahl
geheimnis=1337
versuch=0
while versuch !=geheimnis :
  versuch=int(input("Raten Sie"))
print("Sie haben es geschafft")
#geheime Zahl
geheimnis=9
versuch=0
while versuch !=geheimnis and versuch!=-1:
  versuch=int(input("Raten Sie"))
  if versuch==-1:
   print("Spiel beendet")
  elif versuch ==geheimnis:
   print("Sie haben es geschafft")
  else:
    print("nochmal versuchen")
geheimnis=9
versuch=0
while versuch !=geheimnis and versuch!=-1:
  versuch=int(input("Raten Sie"))
  if versuch==-1:
   print("Spiel beendet")    
   break
else:
 print("Sie haben es geschafft")
print("Ende")
import random
geheimnis=random.randint(1,10)
versuch=None
while versuch!=geheimnis:
  versuch=int(input("Raten Sie:"))
  if versuch ==0:
    print("Das Spiel Wird beendet")
    break
else:
  print("Sie haben es geschafft")
print("Ende")
while True:
  a=int(input("Eine positive zahl:"))
  if a<=0:
    print("die Zahl soll positiv sein")
  else:
    print("richtig")
    break
print("Ende")

  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
kelime=input("Kelime girin: ")
harf=input("harf girin: ")
this_tuple=("a","e","u","ı","o","ü","i","ö")
sayac=0
for sesli in kelime:
  if  harf in this_tuple and sesli==harf:
     sayac+=1
   
print(sayac)
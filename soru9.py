metin=input("Kelime girin: ")
kelime=input("Harf girin: ")
yeni=""
for harf in metin:
  if harf not in kelime:
    yeni+=harf
    
print(yeni)
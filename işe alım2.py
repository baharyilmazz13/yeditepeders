#SOFTWAREFİRMA
note=int(input("Deine Note"))
if note>=90:
  print("Eingestellt")
programmiererfahrung=int(input("Deine Erfahrung 0-5:"))
if programmiererfahrung==5 and note>70:
  print("Eingestellt")
elif programmiererfahrung==4:
  print("Eingeladen")
else:
    print("Ablehnen")
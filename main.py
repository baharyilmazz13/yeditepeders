def kreis (r):
  pi=3.14
  print("Umfang: " + str(2*pi*r))

def kreis_flache(r):
   pi=3.14
   print("Flache: " + str(pi*r*r))

def  zylinder_volumen(r,h):
   pi=3.14
   print("Flache: "+ str(pi*r*r*h))

print("Was möchten Sie? ")
f=int(input("1.Umfang 2.Flache 3.Zylinder"))

if f==1:
  r=float(input("Radius: "))
  kreis(r)
elif f==2:
  r=float(input("Radius: "))
  kreis_flache(r)
else:
  r=float(input("Radius: "))
  h=float(input("Heigh: "))
  zylinder_volumen(r,h)

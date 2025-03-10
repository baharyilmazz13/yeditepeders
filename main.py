#RechnenMaschine
def Add(a, b):
  print(a+b)
def sub(a, b):
  print(a-b)
def div(a, b):
  print(a/b)
def mul(a, b):
  print(a*b)

operator=input("Operation: +, -, *, /")
while True:
 a=float(input("Eine Zahl:"))
 b=float(input("Zweite Zahl:"))
 if operator=="+":
  print("Sonuç:", a+b)
 elif operator=="-":
  print("Sonuç:", a-b)
 elif operator=="*":
  print("Sonuç:", a*b)
 elif operator=="/":
  print("Sonuç:", a/b)
 else:
   print("geçerli işlem değil")
   break
def add(a,b):
  returna+b
def sub(c,d):
  returnc-d
def mul(e,f):
  returne*f
def div(g,h):
  returng/h
print("=================")
print("1.TO PERFORM ADDITION")
print("2.TO PERFORM SUBTRACTION")
print("3.TO PERFORM MULTIPICATION")
print("4.TO PERFORM DIVISION")
print("5.Exit")
print("=================")
while(1):
  choice = int(input("Enter Your choice"))
  if choice ==1:
     a=int(input("Enter the 1st value"))
     b=int(input("Enter the 2nd value"))
     print(add(a,b))
 elif choice ==2:
  e=int(input("Enter the 1st value"))
  d=int(input("Enter the 2nd value"))
  print(sub(c,d))
 elif choice ==3:
  e=int(input("Enter the 1st value"))
  f=int(input("Enter the 2nd value"))
  print(mul(e,f))
 elif choice ==4:
  g=int(input("Enter the 1st value"))
  h=int(input("Enter the 2nd value"))
  print(div(g,h))
 elif choice ==5:
  print("Exited")
  break
 else:
  print("wrong choice")

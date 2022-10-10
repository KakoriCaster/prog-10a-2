from math import *
a=int(input("Ievadiet a: "))
b=int(input("Ievadiet b: "))
c=int(input("Ievadiet c: "))
D=b**2-4*a*c
if D<0:
  print("sakņu nav!")
elif D==0:
 x=-b/2*a
 print("Ir viena sakne =",x)
else:
 x1=(-b+sqrt(D))/2*a
 x2=(-b-sqrt(D))/2*a
print("Ir divas saknes, x1 =",x1," x2 =",x2)
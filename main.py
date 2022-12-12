x=int(input("Введи x: "))
y=int(input("Введи y: "))
if x==0 and y==0:
 print("точка находится в начале оси координат")
if x==0:
 print("точка находится на оси y")
if y==0:
 print("точка находится на оси x")
if x>0 and y>0: print("1 квадрант")
elif x<0 and y>0: print("2 квадрант")
elif x<0 and y<0: print("3 квадрант")
elif x>0 and y<0: print("4 квадрант")
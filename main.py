print("ievadi 3 leņķus")
a=int(input("Ievadiet 1. leņķ: "))
b=int(input("Ievadiet 2. leņķ: "))
c=int(input("Ievadiet 3. leņķ: "))
t=a+b+c
if t>180:
  print("tristuris neeksiste")
if t<180:
  print("tristuris neeksiste")
elif a+b+c==180:
  print("tristuris eksiste")
if a==b==c: print("tas ir vienadmalu tristuris")
elif a==90: print("tas ir taisnleņķa trijstūris")
elif b==90: print("tas ir taisnleņķa trijstūris")
elif c==90: print("tas ir taisnleņķa trijstūris")
if a>90: print("tas ir platleņķa trijstūris")
elif b>90: print("tas ir platleņķa trijstūris")
elif c>90: print("tas ir platleņķa trijstūris")
if a<90 and b<90 and c<90: print("tas ir šaurleņķa trijstūris")
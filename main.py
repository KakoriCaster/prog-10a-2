import math

RulPlat=int(input("Rulona platums: "))
RulGar=int(input("Rulona garums: "))
RulCena=int(input("Rulona Cenu: "))
TelpasGarums=int(input("Telpa Garums: "))
TelpasPlatums=int(input("Telpa platums: "))

RulonaLaukums=RulGar*RulPlat
telpasizmers = math.ceil(TelpasGarums) * math.ceil(TelpasPlatums)
GridaCena=telpasizmers/RulonaLaukums*RulCena

print("izklājot gridas cena:", GridaCena)
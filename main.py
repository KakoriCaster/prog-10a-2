##3.uzd
# alga = int(input("напишите вашу зп:"))
# klientsk = int(input("напишите кол-во обслуженных клиентов:")) # if klientsk >= 5:
#   algafinal = alga + alga/100*25
#   algabonus = alga/100*25
#   print("ваша финальная зарплата:", algafinal)
# if klientsk >= 5:
#   print("надбавка составляет", algabonus, "евро")
# if klientsk < 5:
#     print("надбавки нет :(, ваша зарплата - ", alga, "евро") 
##5.uzd
# day = int(input("впишите порядковый номер дня:"))
# if day > 365 or day < 0:
#   print("вы лох, вкурсе?")
# if day > 0 and day <= 31:
#   print("это январь", day, "число")
# if day > 31 and day <= 59:
#   print("Февраль", day-31, "число")
# if day > 59 and day <= 90:
#   print("это март", day-59, "число")
# if day > 90 and day <= 120:
#   print("это апрель",day-90, "число")
# if day > 120 and day <= 151:
#   print("это май",day-120, "число")
# if day > 151 and day <= 181:
#   print("это июнь",day-151, "число")
# if day > 181 and day <= 212:
#   print("это июль",day-181, "число")
# if day > 212 and day <= 243:
#   print("это август",day-212, "число")
# if day > 243 and day <= 273:
#   print("это сентябрь",day-243, "число")
# if day > 273 and day <= 304:
#   print("это октябрь",day-273, "число")
# if day > 304 and day <= 334:
#   print("это ноябрь",day-304, "число")
# if day > 334 and day <= 365:
#   print("это декабрь",day-334, "число") 
##6.uzd
# stur1 = int(input("1 угол:"))
# stur2 = int(input("2 угол:"))
# stur3 = int(input("3 угол:"))
# if stur1+stur2+stur3 > 180 or stur1+stur2+stur3 <= 0 or stur1+stur2+stur3 < 180:
#   print("вы лох, вкурсе?")
# if stur1 == 90 and stur1+stur2+stur3 == 180 or stur2 == 90  and stur1+stur2+stur3 == 180 or stur3 == 90 and stur1+stur2+stur3 == 180 :
#   print("это прямоугольный треугольник")
# if stur1 > 90 and stur1+stur2+stur3 == 180 or stur2 > 90 and stur1+stur2+stur3 == 180 or stur3 > 90 and stur1+stur2+stur3 == 180:
#   print("это тупоугольный треугольник")
# if stur1==stur2==stur3 and stur1+stur2+stur3 == 180:
#   print("это ровноугольный треугольник") 
##8.uzd
## Вычисление факториала циклом, мы это сделали циклом
# число = int(input("ваше число - (_)! "))
# factorial = 1
# while число > 1:
#     factorial *= число
#     число -= 1
# print(factorial)
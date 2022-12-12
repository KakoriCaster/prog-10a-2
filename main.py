# ●  Funkcijaipasuti_tkreklusir trīs parametri saskaņāar formātupasuti_tkreklus(skaits,apdruka, piegade). Parametrsskaitsir vesels skaitlis(pasūtamo kreklu skaits), parametriapdrukaunpiegadeir simbolu virknes.●  Parametrsapdrukavar būt simbolu virkne, kamatļautas trīs vērtības:TEKSTS,ZIMEvaiFOTO. Cena attiecīgi ir 5 EUR, 7 EUR un 20 EUR.●  Parametrspiegadeir Būla tipa mainīgais (TruevaiFalse). JapiegadeirTrueun kopējāpasūtījuma summa ir mazāka nekā 50 EUR, par piegādi papildus jāmaksā 15 EUR, ja summair 50 EUR vai vairāk, tad piegāde ir par brīvu.●  Pasūtījumiem, kas pārsniedz 100 EUR, tiek piemērota 5 % atlaide no pasūtījuma summas

kreklsk=int(input("Введите кол-во маек: "))
kreklzim=int(input("Введите тип принта (teksts - 1, zime - 2, foto - 3): "))
if kreklzim==1:
  printcena = 5
elif kreklzim==2:
  printcena = 7
elif kreklzim==3:
  printcena = 20
else:
  printcena = 0
  print("Nav tada printa, neiespējami veikt pasūtījumu ")
pascena=kreklsk*printcena
if pascena<50 and kreklzim>0 and kreklzim<4:
  pascena=pascena+15
  print("par piegādi papildus jāmaksā 15 EUR")
print("Цена заказа =", pascena, "евро") 
if pascena>50 or pascena==50:
  pascena=pascena
  print("bezmaksas piegāde")
if pascena>100:
   print("Jums pienākas 5% atlaide! pasutijuma cena:", pascena/100*95,"euro")
"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""
#Kods lai aprēķinātu cilindra tilpumu3
rādiuss = int(input("Ievadiet rādiusu:"))
augstums = int(input("Ievadiet augstumu:"))

tilpums = ((2*3,14*rādiuss) * augstums) + ((3,14*rādiuss**2)*2)
print(tilpums);

laukums = 3,14*(rādiuss*rādiuss);
print(laukums);
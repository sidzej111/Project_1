#BMI hodnoty
# < 18,5	Podvýživa
# 18,5 – 25	Zdravá váha
# 25 – 30	Mírná nadváha
# 30 – 40	Obezita
# 40 <	Těžká obezita

# informace o "testovanem"
jmeno = "Martin"
vaha = 80
vyska = 2

#vypocet BMI
bmi = vaha / vyska ** 2

# podminkovy zapis BMI
if bmi > 40:
    kategorie = "Těžká obezita"
elif bmi > 30:
    kategorie = "Obezita"
elif bmi > 25:
    kategorie = "Mírná nadváha"
elif bmi > 18.5:
    kategorie = "Zdravá váha"
else: 
    kategorie = "Podvýživa"

# vysledek
print(jmeno , "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")
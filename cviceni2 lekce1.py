# cviceni 2 - převaděč jednotek
# Převaděč bude umět následující:
# převod z:
    # kilogramů na libry
    # kilometrů na míle
    # litrů na galony

# Převodní poměry k jednotkám:
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

# Výpočty
kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet

#Výsledky
print(kg_pocet, "kg je", kg_vysledek, "lb")
print(km_pocet, "km je", km_vysledek, "mil")
print(l_pocet, "litru je", l_vysledek, "gal")
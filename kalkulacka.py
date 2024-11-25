# Získávání čísel od uživatele
prvni_cislo = float(input("Zadej první číslo: "))
druhe_cislo = float(input("Zadej druhé číslo: "))
# Získání operace od uživatele
operace = input("Zadej operaci (+, -, *, /): ")
# Zpracování operace a výpočet
if operace == "+":  vysledek = prvni_cislo + druhe_cislo
elif operace == "-":    vysledek = prvni_cislo - druhe_cislo
elif operace == "*":    vysledek = prvni_cislo * druhe_cislo
elif operace == "/":
        if druhe_cislo != 0: vysledek = prvni_cislo / druhe_cislo
        else: vysledek = "Chyba: Dělení nulou není možné!"
else: vysledek = "Chyba: Neplatná operace!"
# Zobrazení výsledku
print("Výsledek je:", vysledek)
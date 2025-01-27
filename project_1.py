'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]






import re

# Seznam registrovaných uživatelů (pro jednoduchost používáme slovník)
uzivatele = {
    "uzivatel1": "heslo1",
    "uzivatel2": "heslo2",
    "uzivatel3": "heslo3"
}

# Funkce pro analýzu textu
def analyzuj_text(TEXTS):
    # Počet slov
    pocet_slov = len(TEXTS.split())
    
    # Počet slov začínajících velkým písmenem
    pocet_velkych_pismen = sum(1 for slovo in TEXTS.split() if slovo[0].isupper())
    
    # Počet slov psaných velkými písmeny
    pocet_velkymi_pismeny = sum(1 for slovo in TEXTS.split() if slovo.isupper())
    
    # Počet slov psaných malými písmeny
    pocet_malych_pismeny = sum(1 for slovo in TEXTS.split() if slovo.islower())
    
    # Počet čísel (ne cifer)
    pocet_cisel = len(re.findall(r'\b\d+\b', TEXTS))
    
    # Suma všech čísel (ne cifer) v textu
    suma_cisel = sum(int(cislo) for cislo in re.findall(r'\b\d+\b', TEXTS))
    
    # Výpis výsledků
    print(f"Počet slov: {pocet_slov}")
    print(f"Počet slov začínajících velkým písmenem: {pocet_velkych_pismen}")
    print(f"Počet slov psaných velkými písmeny: {pocet_velkymi_pismeny}")
    print(f"Počet slov psaných malými písmeny: {pocet_malych_pismeny}")
    print(f"Počet čísel: {pocet_cisel}")
    print(f"Suma všech čísel: {suma_cisel}")

# Funkce pro přihlášení
def prihlaseni():
    uzivatelske_jmeno = input("Zadejte přihlašovací jméno: ")
    heslo = input("Zadejte heslo: ")

    if uzivatelske_jmeno in uzivatele and uzivatele[uzivatelske_jmeno] == heslo:
        print(f"Ahoj, {uzivatelske_jmeno}!")
        return True
    else:
        print("Neplatné přihlašovací údaje. Program bude ukončen.")
        return False

# Hlavní část programu
def hlavni_program():
    if prihlaseni():
        try:
            # Výběr textu pro analýzu
            print("Vyberte číslo textu k analýze:")
            print("1. Text 1")
            print("2. Text 2")
            print("3. Text 3")

            volba = input("Zadejte číslo (1, 2, nebo 3): ")

            # Ověření, že volba je číslo a v rámci povolených
            if not volba.isdigit() or int(volba) not in [1, 2, 3]:
                print("Neplatný výběr. Program bude ukončen.")
                return

            # Předdefinované texty
            texty = {
                1: "Toto je první text, který obsahuje 5 slov a číslo 100.",
                2: "Druhý text má více slov, jako například například tři číselné hodnoty: 20, 30, 40.",
                3: "Třetí text je složitější s velkými a malými písmeny, a číslem 50."
            }

            # Analyzování vybraného textu
            analyzuj_text(texty[int(volba)])

        except ValueError:
            print("Chybný vstup. Program bude ukončen.")

# Spuštění hlavního programu
hlavni_program()

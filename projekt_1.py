"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Polášek
email: sidzej111@seznam.cz
"""

# zadané texty
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

# registrovaní uživatelé
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přihlášení
username = input("username: ")
password = input("password: ")

# ověření údajů pro přihlášení
if username in uzivatele and uzivatele[username] == password:
    print(f'-' * 40)
    print(f"Welcome to the app, {username}")
    print(f"We have 3 texts to be analyzed.")
    print(f'-' * 40)
    
    # výběr čísla textu
    zvolit_cislo = input("Enter a number btw. 1 and 3 to select: ")

    # ověření, zda uživatel vybral číslo (1-3)
    if zvolit_cislo.isdigit():
        zvolit_cislo = int(zvolit_cislo)
        
        if zvolit_cislo < 1 or zvolit_cislo > 3:
            print("Error: Invalid number, terminating the program..")
        else:
            text = TEXTS[zvolit_cislo - 1]
            
            # textová analýza
            words = text.split()
            word_count = len(words)
            titlecase_count = sum(1 for word in words if word[0].isupper())
            uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
            lowercase_count = sum(1 for word in words if word.islower())
            numeric_count = sum(1 for word in words if word.isdigit())
            number_sum = sum(int(word) for word in words if word.isdigit())
            
            # vypsání statistik
            print(
                f"There are {word_count} words in the selected text.\n"
                f"There are {titlecase_count} titlecase words.\n"
                f"There are {uppercase_count} uppercase words.\n"
                f"There are {lowercase_count} lowercase words.\n"
                f"There are {numeric_count} numeric strings.\n"
                f"The sum of all the numbers {number_sum}\n"
                + "-" * 40
            )

            # vytvoření seznamu délek slov
            delky_slov = [len(word) for word in words]
            pocet_delek = {}
            for delka in delky_slov:
                if delka in pocet_delek:
                    pocet_delek[delka] += 1
                else:
                    pocet_delek[delka] = 1
            
            # vypsání délek slov
            print(f"LEN|  OCCURENCES  |NR.")
            print("-" * 40)
            for delka in sorted(pocet_delek.keys()):
                print(f" {delka:2}|{'*' * pocet_delek[delka]:<15} |{pocet_delek[delka]}")
    
    else:
        print("Error: invalid input, terminating the program..")

else:
    print("Unregistered user, terminating the program..")
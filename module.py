# Seznam registrovaných uživatelů
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty pro analýzu
TEXTS = [
'''
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

# Funkce pro analýzu textů
def analyze_text(TEXTS):
    # Uživatel si vybere text, který chce analyzovat
    try:
        choice = int(input("Enter a number between 1 and 3 to select: "))
        
        if choice < 1 or choice > 3:
            print("Invalid choice, terminating the program..")
            return  # Ukončíme funkci, pokud volba není validní
        else:
            # Vybereme text podle volby uživatele
            text = TEXTS[choice - 1]
            
            # Rozdělíme text na slova (oddělená mezerami)
            words = text.split()
            
            # Počet slov
            word_count = len(words)
            
            # Počet slov začínajících velkým písmenem
            titlecase_count = sum(1 for word in words if word[0].isupper())
            
            # Počet slov psaných velkými písmeny
            uppercase_count = sum(1 for word in words if word.isupper())
            
            # Počet slov psaných malými písmeny
            lowercase_count = sum(1 for word in words if word.islower())
            
            # Počet čísel
            numeric_count = sum(1 for word in words if word.isdigit())
            
            # Suma všech čísel
            number_sum = sum(int(word) for word in words if word.isdigit())
            
            # Vytisknutí statistik
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numeric_count} numeric strings.")
            print(f"The sum of all the numbers {number_sum}")
            
    except ValueError:
        print("Invalid input, must be a number, terminating the program..")
        return  # Pokud uživatel zadá neplatný vstup

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

# Ověření přihlašovacích údajů
if username in users and users[username] == password:
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    
    # Zavoláme funkci pro analýzu textů
    analyze_text(TEXTS)
else:
    print("unregistered user, terminating the program..")
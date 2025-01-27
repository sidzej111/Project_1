# Seznam uživatelů
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',
    
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

# Funkce pro analýzu textu
def analyze_text(text):
    # Rozdělení textu na slova
    words = re.findall(r'\b\w+\b', text)
    
    # Počet slov
    word_count = len(words)
    
    # Počet slov začínajících velkým písmenem
    titlecase_count = sum(1 for word in words if word.istitle())
    
    # Počet slov psaných velkými písmeny
    uppercase_count = sum(1 for word in words if word.isupper())
    
    # Počet slov psaných malými písmeny
    lowercase_count = sum(1 for word in words if word.islower())
    
    # Počet čísel (ne cifer)
    numeric_strings = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine|zero|[0-9]+)\b', text, re.IGNORECASE)
    numeric_count = len(numeric_strings)
    
    # Suma všech čísel
    numbers = re.findall(r'\b\d+\b', text)
    number_sum = sum(int(num) for num in numbers)
    
    # Vytisknutí statistik
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {number_sum}")
    
    # Generování grafu pro délky slov
    word_lengths = [len(word) for word in words]
    length_counts = Counter(word_lengths)
    
    print("\nLEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    max_length = max(length_counts.keys())
    for length in range(1, max_length + 1):
        count = length_counts.get(length, 0)
        print(f"{length:2}|{'*' * count:<12}|{count}")

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

# Ověření přihlašovacích údajů
if username in users and users[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    
    # Výběr textu
    try:
        choice = int(input("Enter a number btw. 1 and 3 to select: "))
        
        if choice not in [1, 2, 3]:
            print("Invalid choice, terminating the program..")
        else:
            print("----------------------------------------")
            analyze_text(TEXTS[choice - 1])  # Vybereme text podle volby uživatele
    except ValueError:
        print("Invalid input, must be a number, terminating the program..")
else:
    print("unregistered user, terminating the program..")
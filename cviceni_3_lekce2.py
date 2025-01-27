# List zaměstnanci
zamestnanci = ["František", "Anna", "Jakub", "Klara"]

# Výpis listu zaměstnanci
print("Zaměstnanci na začátku:", zamestnanci)

# kopie listu zamestnanci a přidání nových jmen
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anezka")

# vypsání obsahu listu zamestnanci_a
print("Nová jména přidána:", zamestnanci_a)

# kopie a vložení jména "Bruno" na index 1
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")

# výpis seznamu zamestnanci_b
print("Nová jména vložena:", zamestnanci_b)
# seznam zamestnancu
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]

# posledni index
posledni_index = len(zamestnanci) -1

# vypsat jmeno na indexu2
print("Na indexu 2 je:", zamestnanci[2])

# vypsat posledni index
print("Na", posledni_index, "indexu je:", zamestnanci[posledni_index])

# vypsat index od 2 do 5
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])

# vypsat každý třetí prvek listu zamestnanci
print("Každý třetí člen je:", zamestnanci[::3])
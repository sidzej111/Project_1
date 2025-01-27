#proměnná
user_email = {"email": "marek.parek@gmail.com"}

# nový prázdný slovník 
user_1 = dict()

# přidání klíčů a hodnot
user_1["name"] = "Marek"
user_1["surname"] = "Parek"

# rozšíření slovníku pomocí metody "update"
user_1.update(user_email)

# vypsání hodnot s doplňujícím textem
print("User #01:", user_1)
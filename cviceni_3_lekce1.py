# cviceni 3 - provest ruzne operace s datovym typem "str" a "int"

# Úloha musí splňovat následující

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = (rolls_royce * 2) + (vybava * 2)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

# Sleva na Mercedes
print("Sleva na mercedes je", sleva_merc)
print("Cena za dva mercedesy je", cena_2_merc)
print("Cena za mercedes a rolls royce je", cena_merc_a_rolls)
print("Cena za dva rolls royce s vybavou je", cena_2_rolls_s_vybavou)
print("Cena za mercedes s vybavou je", cena_merc_s_vybavou)
print("Cena za mercedes se slevou je", merc_se_slevou)
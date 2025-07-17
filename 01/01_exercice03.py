# Bosolindo Edhiengene Roger
# rogerbosolinndo34@gmail.com
# L2 Génie électrique
# ================================

heures = int(input("Nombre d'heures : "))
minutes = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes"))

# conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# Résultat
print(f"Durée totale : {total_secondes} secondes")

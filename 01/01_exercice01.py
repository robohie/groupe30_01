# Bosolindo Edhiengene Roger
# rogerbosolinndo34@gmail.com
# L2 Génie électrique
# ================================

prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# Approximation des jours vécus
jours = age * 365

# Affichage formaté
print(f"=== PROFIL UTILISATEUR ===")
print(f"Prénom {prenom}")
print(f"Age : {age} ans ({jours} jours vécus environ)")
print(f"Ville : {ville}")
print(f"métier : {metier}")

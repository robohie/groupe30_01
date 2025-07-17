# Bosolindo Edhiengene Roger
# rogerbosolinndo34@gmail.com
# L2 Génie électrique
# ================================

distance_km = float(input("Distance(km) : "))
temps_h = float(input("Temps(heures) : "))

vitesse_kmh = distance_km / temps_h
vitesse_ms = vitesse_kmh * 1000 / 3600

print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"vitesse moyenne : {vitesse_ms:.2f} m/s")

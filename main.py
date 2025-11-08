import math

longueur = int(input("Indiquer la longueur à protéger: "))
barreau = int(input("Indiquer la section des barreaux: "))

nbarreau = math.ceil((longueur-110)/(110+barreau))
clair = (longueur-barreau*nbarreau)/(nbarreau+1)

print ("Nombre de barreaux: ",nbarreau)
print("--------------------------------")
print("RAPPEL: le clair doit être < 110 mm")
print("--------------------------------")
print ("Le clair sera de: ",round(clair,2))

#programme recherche des nombres paires
try:
    num =input("Boujour visiteur, veuillez entrez un nombre(exemple 20) et ce programme vous affichera la liste des nombres pairs de zéro à celui ci: ")
    for num_pairs in range(0,int(num) + 1,2):
        print(f" {num_pairs} est un nombre pair dans l'intervalle 0 à {num}")
except ValueError:
    print("Veuillez entrer le nombre en chiffre et sans caractère") 

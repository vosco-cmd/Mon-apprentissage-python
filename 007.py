print("Ce programme sert à répartir de façon proportionnelle le poids de different charette") 
nb_charrettes = int(input("Entrer le nombre de charrettes : "))
poids_charrettes = [0.0] * nb_charrettes
poids_total = 0.0
print("Entrer successivement le poids de chaque charettes")                         
for id_charrette in range(nb_charrettes):
   poids_actuel = float(input())
   poids_total = poids_total + poids_actuel
   poids_charrettes[id_charrette] = poids_actuel
moyenne_poids = poids_total / nb_charrettes
for id_charrette in range(nb_charrettes):
   poids_charrettes[id_charrette] = moyenne_poids
   print(poids_charrettes[id_charrette])

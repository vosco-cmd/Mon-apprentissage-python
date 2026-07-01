#Cet exercice était difficile et je pèse mes mots. J'ai dû comprendre la gestion des variables booléennes et la synchronisation des boucles while pour éviter les crashs à la dernière ligne.
total_envisages = int(input())
temp_minimal = int(input())
temp_maximal = int(input())
temp_relevee = int(input())
pas_alarme = (temp_minimal <= temp_relevee) and (temp_relevee <= temp_maximal)
while pas_alarme and total_envisages > 0:
   print("Rien à signaler")
   total_envisages = total_envisages - 1
   if total_envisages > 0:
      temp_relevee = int(input())
      pas_alarme = (temp_minimal <= temp_relevee) and (temp_relevee <= temp_maximal)
if not pas_alarme:
   print("Alerte !!")

print("Bonjour utilisateur, ce programme vous permet d'afficher la table de multiplication de l'entier de votre choix.")
x = int(input("Entrez votre multiple: "))
print(f"La table de multiplication de {x} à 10 est :")
for i in range(1,11):
      print(f"{i} X {x} = {i*x}")

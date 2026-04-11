print("Boujour visiteur, ce programme est une caculatrice basique capable d'effectuer des divisions, des multiplications, des additions et des soustractions.")
while True:
    print("  division, multilplication, addition, soustraction")
    operateur = input("Entrez lequelle de ces operation souhaiteriez faire : ")
    if operateur == "division":
        a = float(input("Entrez la dividante(nombre qui sera divisez) : "))
        b = float(input("Entrez le diviseur (nombre qui divise) : "))
        print(f"{a} ÷ {b} = {a/b} ")
        rep = input("Voudriez vous faire en un autre cacul(y/n) : ")
        if rep == "n": break
    if operateur == "multiplication":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le second : "))
        print(f"{a} X {b} = {a*b}") 
        rep = input("Voudriez vous faire en un autre cacul(y/n) : ")
        if rep == "n": break
    if operateur == "addition":
        a = float(input("Entrez votre premier nombre : "))
        b = float(input("Entrez votre second : ")) 
        print(f"{a} + {b} = {a+b}") 
        rep = input("Voudriez vous faire en un autre cacul(y/n) : ")
        if rep == "n": break
    if operateur == "soustraction":
        a = float(input("Entrez votre premier nombre : "))
        b = float(input("Entrez votre second : ")) 
        print(f"{a} - {b} = {a-b}") 
        rep = input("Voudriez vous faire en un autre cacul(y/n) : ")
    
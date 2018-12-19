import os
def fibo():
    limite = int(raw_input("Choisir a quel nombre s'arreter : "))
    a = 0
    b = 1
    resultat = 0
    print(a)
    print(b)
    while resultat <= limite:
        resultat = a+b
        a = b
        b = resultat
        resultat = a + b
        print(resultat)


def main():
    banner = """
d88888b d888888b d8888b.  .d88b.          d8888b. d88888b .88b  d88. d888888b
88'       `88'   88  `8D .8P  Y8.         88  `8D 88'     88'YbdP`88   `88'  
88ooo      88    88oooY' 88    88         88oobY' 88ooooo 88  88  88    88   
88~~~      88    88~~~b. 88    88         88`8b   88~~~~~ 88  88  88    88   
88        .88.   88   8D `8b  d8'         88 `88. 88.     88  88  88   .88.  
YP      Y888888P Y8888P'  `Y88P'          88   YD Y88888P YP  YP  YP Y888888P

"""
    os.system("cls")
    print(banner)
    fibo()


### --- Lancement de la fonction Main ---###
main()
    
    


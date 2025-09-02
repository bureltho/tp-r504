import fonctions as f

while True:
    try:
        a = int(input("Choisi un nombre : "))
        b = int(input("Son exposant: "))
        res = f.puissance(a, b)
        print(f"{a} puissance {b} = {res}")
    except ValueError:
        print("Veuillez saisir des entiers valides.")
    except TypeError as e:
        print(f"Erreur : {e}")


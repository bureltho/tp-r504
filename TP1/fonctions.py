def puissance(a: int, b: int) -> int | float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Seuls les entiers sont autorisés")

    if a == 0 and b < 0:
        raise ValueError("On ne peut pas avec 0")

    if b == 0:
        return 1

    if b > 0:
        resultat = 1
        for _ in range(b):
            resultat *= a
        return resultat

    if b < 0:
        resultat = 1
        for _ in range(-b):
            resultat *= a
        return 1 / resultat

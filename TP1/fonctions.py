def puissance(a: int, b: int) -> int:
    if not type(a) is int:
        raise TypeError("Le premier argument doit être un entier (int).")
    if not type(b) is int:
        raise TypeError("Le second argument doit être un entier (int).")
    return a ** b

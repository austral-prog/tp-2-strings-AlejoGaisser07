def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingrese un nombre: ")
    nombre_minusc = nombre.lower()
    print(f"Contiene a: {'a' in nombre_minusc}")
    print(f"Contiene e: {'e' in nombre_minusc}")
    print(f"Contiene i: {'i' in nombre_minusc}")
    print(f"Contiene o: {'o' in nombre_minusc}")
    print(f"Contiene u: {'u' in nombre_minusc}")

check_vowels()



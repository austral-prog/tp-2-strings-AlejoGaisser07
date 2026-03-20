def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass

    base = int(input("Ingrese la base de un rectángulo: "))
    altura = int(input("Ingrese la altura de un rectángulo: "))
    area = base * altura
    perimetro = base*2 + altura*2
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")

rectangle()
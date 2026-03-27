def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingrese cuanto dinero gastó: "))
    dinero = int(input("Ingrese cuanto dinero recibió: "))
    gasto_total = dinero - gasto
    pesos = int(gasto_total)
    centavos = round((gasto_total - pesos)*100)
    
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

#change()
    
    
    
def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("Ingrese un precio: "))
    descuento = float(input("Ingrese un descuento: "))
    cantidad = int(input("Ingrese una cantidad: "))
    
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio - descuento}")
    print(f"Total: {(precio - descuento) * cantidad}")

casting()

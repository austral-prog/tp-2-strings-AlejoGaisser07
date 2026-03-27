def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    
    nombre = input("Ingrese su nombre completo: ")  # Declaro los inputs
    email = input("Ingrese su email: ")
    nota1 = int(input("Ingrese su 1era nota: "))
    nota2 = int(input("Ingrese su 2da nota: "))
    nota3 = int(input("Ingrese su 3era nota: "))
    
    decoracion = "=" * 24
    nombre_strip = nombre.strip() # Saca cualquier espacio que haya puesto el usuario 
    titulo = f"{decoracion}\n{'FICHA DEL ALUMNO'.center(24).rstrip()}\n{decoracion}" # Titulo
    len_nombre = len(nombre_strip) # Cuento los caracteres del nombre
    partes = nombre_strip.find(' ') # Encuentra el espacio de en medio
    iniciales = nombre_strip[0] + nombre_strip[partes+1] # calcula las iniciales
    dominio_email = email[email.find('@')+1:].lower() # busca a partir del @, uno más y en minúscula
    codigo_secreto = nombre_strip[::-1].upper() # Pongo el nombre al revés en mayúscula
    suma_notas = nota1 + nota2 + nota3
    
    print(titulo)
    print(f"Nombre: {nombre.title().strip()}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len_nombre}")
    print(f"Iniciales: {iniciales.upper()}") # Convierto las iniciales a mayusc.
    print(f"Usuario: {nombre_strip[partes+1:].lower()}.{nombre_strip[0:partes].lower()}") # desde el espacio hasta el final + . + desde el principio hasta el espacio
    print(f"Email valido: {'@' in email}") # Que me devuelva True si tiene el @
    print(f"Dominio: {dominio_email}") # Printea todo despues del @
    print(f"Nombre para archivo: {nombre_strip.replace(' ', '_').title()}") # que remplace el espacio de en medio por un _
    print(f"Cantidad de a: {nombre_strip.lower().count('a')}") # Cuenta las a, primero convierto a minusc.
    print(f"Codigo secreto: {codigo_secreto}") 
    print(f"Nota 1: {nota1}\nNota 2: {nota2}\nNota 3: {nota3}")
    print(f"Suma: {suma_notas}")
    print(f"Promedio: {suma_notas/3}")
    print(f"Promedio entero: {suma_notas//3}")
    print(decoracion)

#ficha()
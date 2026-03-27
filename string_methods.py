def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""
    
    print(f"Strip: {nombre.strip()}") # saco los posibles espacios externos
    print(f"Lstrip: {nombre.lstrip()}") # saco solo por izquierda los espacios
    print(f"Rstrip: {nombre.rstrip()}") # saco por derecha los espacios
    print(f"Upper: {frase.upper()}") # la convierto a mayusc.
    print(f"Lower: {frase.lower()}") # la convierto a minusc.
    print(f"Title: {frase.title()}") # hago formato title
    print(f"Find: {frase.find('gran')}") # Busca la primera posicion de la palabra "gran"
    print(f"Replace: {frase.replace('programacion', 'desarrollo')}") # Cambia la palabra "programación" por la palabra "desarrollo"
    print(f"Count: {frase.count('a')}") # cuenta las "a"
    print(f"Contiene Python: {'Python' in frase}") # Devuelve un bool si está en frase
    print(f"Contiene Java: {'Java' in frase}") # ""
    print(f"Slice: {frase[:6]}") # primera posición a la 5ta incluido
    print(f"Paso: {frase[:6:2]}") # "" de 2 en 2
    print(f"Reverso: {frase[5::-1]}") # va al reves y hasta la posición 5
    print(f"Formato: {nombre.strip()} sabe Python") # f-string para poner el nombre en una frase
    print(f"{multilinea}") 
    
string_methods()
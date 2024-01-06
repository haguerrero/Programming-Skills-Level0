def account():
    print("Ingrese los datos del cliente: ")
    name = input("Nombre: ")

    while not name.isalpha():
        print("El nombre debe ser solo caracteres")
        name = input("Nombre: ")
    
    last_name = input("Apellio: ")
    
    while not last_name.isalpha():
        print("El apellido debe ser solo caracteres")
        last_name = input("Apellio: ")

    return name, last_name

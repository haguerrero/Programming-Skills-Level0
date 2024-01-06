import create

def menu():
    options = ["1. Crear cuenta", "2. Transferir", "3. Ver estado de cuenta", "0. Salir"]

    while True:
        for option in options:
            print(option)

        option = input("Seleccione una opción: ")
        
        if option == "1":
            # Logica crear cuenta
            name, last_name = create.account()
            if name and last_name:
                print("")
                print("**********************************")
                print("La cuenta ha sido creada con exito")
                print("**********************************")
                print("")
            else:
                print("Error al crear la cuenta")
        
        elif option == "2":
            # Logica transferir
            print("Tranferir a otras cuentas")

        elif option == "3":
            # Logica transferir
            print("Otra opción pendiente")
        
        elif option == "0":
            print("")
            print("Hasta luego...")
            print("")
            break
    
if __name__ == "__main__":
    menu()
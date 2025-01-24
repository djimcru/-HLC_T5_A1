""" contraseña = 'secreta123'
intento1 = input('Introduce la contraseña: ')
if intento1 == contraseña:
    print('Has puesto la contraseña a la primera.')
else:
    print('la contraseña es incorrecta ')
    intento2 = input('Introduce la contraseña: ')
    if intento2 == contraseña:
        print('Has puesto la contraseña a la segunda.')
    else:
        print('la contraseña es incorrecta ')
        intento3 = input('Introduce la contraseña: ')
        if intento3 == contraseña:
            print('Has puesto la contraseña a la tercera.')
        else :
            print('No has puesto la contraseña correcta.')
 """
""" intentos = 0
while intentos < 3:
    contraseña = input("Introduce tu contraseña: ")
    if contraseña == "secreta123":
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        intentos += 1
        print(f"Intento {intentos}: Contraseña incorrecta.")
else:
    print("¡Has agotado tus intentos!") """
    def check_pass():
        sistem_pass="secreta123"
        intentos=0

        while intentos <3:
            user_pass=input('Introduce la contraseña: ')
            if sistem_pass == user_pass:
                print('bienvenido')
                break
            else:
                intentos += 1

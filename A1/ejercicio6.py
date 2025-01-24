numero1=int(input('introduce un numero '))
numero2=int(input('introduce otro numero '))
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero2 > numero1:
    print(numero2, "es mayor que", numero1)
elif numero1 == numero2 or numero2 == numero1:
    print("los numeros son iguales")
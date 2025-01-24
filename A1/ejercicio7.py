def suma():
    numero1=int(input('introduce un numero '))
    numero2=int(input('introduce otro numero '))
    suma=numero1+numero2
    return suma
def mostrarSuma():
    resultado=suma()
    print('la suma es ', resultado)
mostrarSuma()
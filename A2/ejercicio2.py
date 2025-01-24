num1=int(input('introduce un numero '))
num2=int(input('introduce un numero '))
num3=int(input('introduce un numero '))
if num1 > num2 and num1 > num3:
    print ("El número 1 es mayor" )
elif num2 > num1 and num2 > num3:
    print ("El número 2 es mayor" )
elif num3 > num1 and num3 > num2:
    print ("El número 3 es mayor" )
else:
    print( "Hay un empate entre dos o más números.")


def comprobar():
    palabra=input('Introduce la palabra: ')

    for char in palabra:
        if "@" ==char:
            print('La palabra tiene el caracter @')
        elif "#" == char:
            print('La palabra tiene el caracter #')
        elif '$' == char:
            print('La palabra tiene el caracter #')
        elif '%' == char:
            print('La palabra tiene el caracter %')

comprobar()
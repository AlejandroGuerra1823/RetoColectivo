def obtenerMedidas( ancho, alto ):
    print()

    print (f'Area: {ancho*alto}')
    print (f'Perimetro: {(ancho *2 )+ (alto * 2)}')

    print()

    for i in range(alto):
        print("*" * ancho)
        
    print()


ancho = int(input('Digite el ancho de sus nalgas: '))

alto = int(input('Digite el alto de sus nalgas: '))


obtenerMedidas(ancho, alto)



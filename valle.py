'''
El valle de aburra afronta altas temperaturas año tras año, Cree una que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura.
'''

def temperaturaPromedioMedellin():
    
    acumulador = 0
    listaTemperatura = []

    for i in range(20):
        temperaturaHoy = int(input("Digita la temperatura de hoy:  "))
        listaTemperatura.append(temperaturaHoy)

    acumulador = sum(listaTemperatura)

    print(f'El promedio de la temperatura de medellin es: {acumulador /20}')

temperaturaPromedioMedellin()
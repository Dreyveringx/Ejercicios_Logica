#Diseñar un algoritmo que lea un número entre 1 y 7, muestre en el resultado domingo si digita 1, lunes si digita 2, martes si digita 3, miércoles si digita 4 jueves si digita 5, viernes si digita 6 y sábado si digita 7. 


numero = int(input("Ingrese un número entre 1 y 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Lunes")
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miércoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sábado")
else:
    print("Número no válido. Debe estar entre 1 y 7.")

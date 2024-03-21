#Diseñar un algoritmo  lea la edad de una persona e indique si puede tener licencia de conducción de vehículo particular o servicio publico.


edad = int(input("Ingrese su edad: "))
tipo_vehiculo = input("¿Qué tipo de vehículo desea conducir (particular/publico)? ").lower()


if tipo_vehiculo == "particular":
    if edad >= 16:
        print("Puede obtener licencia para conducir vehículo particular.")
    else:
        print("No cumple con la edad mínima para obtener licencia de vehículo particular.")
elif tipo_vehiculo == "publico":
    if edad >= 18:
        print("Puede obtener licencia para conducir vehículo de servicio público.")
    else:
        print("No cumple con la edad mínima para obtener licencia de vehículo de servicio público.")
else:
    print("Tipo de vehículo no válido.")

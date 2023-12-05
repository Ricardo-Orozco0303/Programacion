print("*******************************************************")
print("*Bienvenido al sistema vacacional de coca-cola company*")
print("******************************************************* \n")

print("¿Cual es el nombre del trabajador?: ")
Nombre = (input())
print("")
print("¿Cuanto tiempo de servicio tiene el tabajador?: ")
antiguedad = int (input())
print("")
print("¿Cules la clave del tabajador ?: ")
clave = (input())
print("")
if clave == "1":
    if antiguedad == 1:
        print("El trabajador " + Nombre + " tiene derecho a 6 días de vacaciones")
    elif 2 <= antiguedad <= 6:
        print("El trabajador " + Nombre + " tiene derecho a 14 días de vacaciones")
    elif antiguedad >= 7:
        print("El trabajador " + Nombre + " tiene derecho a 20 días de vacaciones")

elif clave == "2":
    if antiguedad == 1:
        print("El trabajador " + Nombre + " tiene derecho a 7 días de vacaciones")
    elif 2 <= antiguedad <= 6:
        print("El trabajador " + Nombre + " tiene derecho a 15 días de vacaciones")
    elif antiguedad >= 7:
        print("El trabajador " + Nombre + " tiene derecho a 22 días de vacaciones")

elif clave == "3":
    if antiguedad == 1:
        print("El trabajador " + Nombre + " tiene derecho a 10 días de vacaciones")
    elif 2 <= antiguedad <= 6:
        print("El trabajador " + Nombre + " tiene derecho a 20 días de vacaciones")
    elif antiguedad >= 7:
        print("El trabajador " + Nombre + " tiene derecho a 30 días de vacaciones")

print("*******************************************************")
print("*Bienvenido al sistema vacacional de coca-cola company*")
print("******************************************************* \n")

print("¿Cual es el nombre del trabajador?: ")
Nombre = (input())
print("")
print("¿Cuanto tiempo de servicio tiene el tabajador?: ")
antiguedad = (input())
print("")
print("¿Cules la clave del tabajador ?: ")
clave = (input())
print("")
if clave == 1 :
    if antiguedad == 1 :
       print("El trabajador " + Nombre + "tiene derecho a 6 dias de vacaciones")
    elif antiguedad >= 2 and antiguedad <= 6 :
       print("El trabajador " + Nombre + "tiene derecho a 14 dias de vacaciones")
    elif antiguedad >= 7:
       print("El trabajador " + Nombre + "tiene derecho a 20 dias de vacaciones")
     	
    if clave == 2 :
        if antiguedad == 1:
            print("El trabajador " + Nombre + "tiene derecho a 7 dias de vacaciones")
        elif antiguedad >= 2 and antiguedad <= 6 :
            print("El trabajador " + Nombre + "tiene derecho a 15 dias de vacaciones")
        elif antiguedad >= 7 :
            print("El trabajador " + Nombre + "tiene derecho a 22 dias de vacaciones")
    

    else if (clave == 3)

      if(antiguedad == 1){
       System.out.printl("Eltrabajador " + nombre + "tiene derecho a 10 dias de vacaciones");
     } else if(antiguedad >= 2 and antiguedad <= 6){
       System.out.printl("Eltrabajador " + nombre + "tiene derecho a 20 dias de vacaciones");
     } else if(antiguedad >= 7){
       System.out.printl("Eltrabajador " + nombre + "tiene derecho a 30 dias de vacaciones");
     }
   
    else 
    System.out.printl("Error la clave de departamento es incorrecta ");

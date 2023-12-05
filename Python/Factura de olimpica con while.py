print("**********************************************************************************")
print("**********Bienvenido al sistema de facturacion de Supermercados olimpica**********")
print("********************************************************************************** \n")
while True:
    opcion = input("¿Deseas agregar un producto? (s/n): ")
    
    if opcion.lower() != 's':
        break
    codigo = input("Ingrese el código del producto: ")
    print("Ingresa el nombre del Producto: ")
    producto = str(input())
    print("Ingresa el valor del Producto: ")
    producto_Cantidad = int (input())
    print("Ingresa la unidad comprada del Producto: ")
    producto_unidad = int (input())
print("**********************************************************************************")
print("**********Bienvenido al sistema de facturacion de Supermercados olimpica**********")
print("********************************************************************************** \n")
productos = []
factura = []
while True:
    opcion = input("¿Deseas agregar un producto? (s/n): ")
    
    if opcion == 'n':
        break
    print("Ingrese el código del producto: ")
    codigo = input()
    print("Ingresa el nombre del Producto: ")
    producto = str(input())
    print("Ingresa el valor del Producto: ")
    valor_producto = int (input())
    print("Ingresa la unidad comprada del Producto: ")
    producto_unidad = int (input())
    productos.append({"nombre": producto, "valor_producto": valor_producto})
    factura.append({"nombre": producto, "producto_unidad": producto_unidad, "subtotal": valor_producto * producto_unidad})
if factura:
    print("*****************************")
    print("********** Factura **********")
    print("***************************** \n")

    for item in factura:
        print(f"{item['nombre']} x{item['producto_unidad']}: ${item['subtotal']}")

    total = sum(item['subtotal'] for item in factura)
    print("*******************")
    print(f"Total: ${total}")
    print("*******************")
else:
    print("No se han ingresado productos. La factura está vacía.")
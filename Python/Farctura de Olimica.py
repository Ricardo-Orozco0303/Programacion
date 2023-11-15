print("Ingresa el nombre del Primer Producto")
producto_1 = str(input())
print("Ingresa el valor del Primer Producto")
producto_1_Cantidad = int (input())
print("Ingresa la unidad comprada del Primer Producto")
producto_1_unidades = int (input())

print("Ingresa el nombre del segundo Producto")
producto_2 = str(input())
print("Ingresa el valor del segundo Producto")
producto_2_Cantidad = int (input())
print("Ingresa la unidad comprada del segundo Producto")
producto_2_unidades = int (input())

print("Ingresa el nombre del tercer Producto")
producto_3 = str(input())
print("Ingresa el valor del tercer Producto")
producto_3_Cantidad = int (input())
print("Ingresa la unidad comprada del tercer Producto")
producto_3_unidades = int (input())

producto_1_st = producto_1_Cantidad * producto_1_unidades
producto_2_st = producto_2_Cantidad * producto_2_unidades
producto_3_st = producto_3_Cantidad * producto_3_unidades

subTot = producto_1_st + producto_2_st + producto_3_st

IVA = subTot * 0.19

total = subTot + IVA

print(" El total a pagar por",producto_1,"es:",producto_1_st)
print(" El total a pagar por",producto_2,"es:",producto_2_st)
print(" El total a pagar por",producto_3,"es:",producto_3_st)
print("El subtotal de la factura es :",subTot)
print("El IVA fue de :",IVA)
print("El total a pagar con IVA es", total)


print("********Bienvenido al experimento de richard********")
print("Marcar segun la operacio a realizar")
print("+ para sumar")
print("- para restar")
print("/ para dividir")
print("* para multiplicar")
print("% para dar un porcentaje ten en cuenta que el primer numero es el que va a operar al segundo")
opcion = (input("Elige una opcion para operar\n"))
print("ahora necesito los dos numeros a operar")
print("ingresa el Primer numero a operar")
Numero_uno = int(input())
print("ingresa el Segundo numero a operar")
Numero_dos = int(input())
if opcion ==  "+" :
    Resultado = Numero_uno + Numero_dos
    print("El resultado de tu suma es: " +  str (Resultado) )
    print("Gracias por usar la calculadora de richard") 
elif opcion ==  "-" :
    Resultado = Numero_uno - Numero_dos
    print("El resultado de tu resta es: " +  str (Resultado) )
    print("Gracias por usar la calculadora de richard")
elif opcion ==  "*" :
    Resultado = Numero_uno * Numero_dos
    print("El resultado de tu multiplicacion es: " +  str (Resultado) )
    print("Gracias por usar la calculadora de richard")
elif opcion ==  "/" :
    Resultado = Numero_uno / Numero_dos
    print("El resultado de tu divicion es: " +  str (Resultado) )
    print("Gracias por usar la calculadora de richard")
elif opcion ==  "%" :
    Resultado = Numero_uno * Numero_dos / 100
    print("El resultado de tu divicion es: " +  str (Resultado) )
    print("Gracias por usar la calculadora de richard")
else :
    print("Por favor revisa lo que digitaste y vuelve a intentarlo ") 
    
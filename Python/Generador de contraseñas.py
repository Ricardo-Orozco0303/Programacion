import random
import string

def generador(longitud):
    Caracteres = string.ascii_letters + string.digits 
    contraseña = ''.join(random.choice(Caracteres) for _ in range(longitud))
    return contraseña
if __name__ == "__main__":
    try:
        longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
        if longitud <= 0:
            raise ValueError("Longitud de la contraseña debe ser un número positivo")
        contraseña_generada = generador(longitud)
        print(f"\nContraseña generada: {contraseña_generada}")
    except ValueError as e :
        print(f"Error{e}")
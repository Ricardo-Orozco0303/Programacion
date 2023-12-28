import tkinter as tk 
from tkinter import messagebox

def inicio_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario == "usuario" and contraseña == "contraseña":
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas")
        

def mensaje_registro():
    messagebox.showinfo("Registro", "¡Usuario registrado con éxito!")

def registro():
    ventana_registro = tk.Toplevel(window)
    ventana_registro.title("Ventana de Registro")

    ancho_ventana_registro = 350
    altura_ventana_registro = 250

    ancho_pantalla = ventana_registro.winfo_screenwidth()
    altura_pantalla = ventana_registro.winfo_screenheight()

    x = (ancho_pantalla - ancho_ventana_registro) // 2
    y = (altura_pantalla - altura_ventana_registro) // 2

    ventana_registro.geometry(f"{ancho_ventana_registro}x{altura_ventana_registro}+{x}+{y}")
    
    label_texto = tk.Label(ventana_registro, text=" Registro ", font=("Times New Roman", 20) )
    label_texto.place(x=120 , y=0)
    
    label_usuario = tk.Label(ventana_registro, text=" Usuario ", font=("Times New Roman", 20) )
    label_usuario.place(x=15, y=45)
    entry_usuario = tk.Entry(ventana_registro)
    entry_usuario.place(x=25, y=80)
    
    label_contraseña = tk.Label(ventana_registro, text=" Contraseña ", font=("Times New Roman", 20) )
    label_contraseña.place(x=15, y=120)
    entry_contraseña = tk.Entry(ventana_registro, show="*")
    entry_contraseña.place(x=25, y=160)

    boton_registrar = tk.Button(ventana_registro, text="Registrar", command=mensaje_registro)
    boton_registrar.place(x=275, y=200)


def mensaje_registro():
    messagebox.showinfo(" Ventana de Registro "," ¡Usuario registrado con éxito! ")
  
window = tk.Tk()

window.title(" Sistema de prueba ")

ancho_ventana = 750
altura_ventana = 500

ancho_pantalla = window.winfo_screenwidth()
altura_pantalla = window.winfo_screenheight()

x = (ancho_pantalla - window.winfo_reqwidth()) // 3
y = (altura_pantalla - window.winfo_reqheight()) // 3

window.geometry("{}x{}+{}+{}".format(ancho_ventana, altura_ventana, x, y))

label_1 = tk.Label(window, text=" Bienvenido a el sistema de prueba ", font=("Times New Roman", 20) )
label_1.place(x=180 , y=0)

label_usuario = tk.Label(window, text=" Usuario ", font=("Times New Roman", 20) )
label_usuario.place(x=300, y=85)
entry_usuario = tk.Entry(window)
entry_usuario.place(x=310, y=130)

label_contraseña = tk.Label(window, text=" contraseña ", font=("Times New Roman", 20) )
label_contraseña.place(x=300, y=175)
entry_contraseña = tk.Entry(window, show="*")
entry_contraseña.place(x=310, y=220)

button = tk.Button(window, text="Iniciar sesion ",command= inicio_sesion)
button.place(x=375, y=300)


button = tk.Button(window, text=" registrarte ", command=registro)
button.place(x=280, y=300)


window.mainloop()
import sqlite3
import tkinter as tk 
from tkinter import messagebox
from escpos.printer import Network

connection = sqlite3.connect("Base_de_prueba.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prueba (
        usuario TEXT,
        contraseña TEXT
    )
''')


def inicio_sesion():

    connection = sqlite3.connect("Base_de_prueba.db")
    cursor = connection.cursor()

    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    try:
        cursor.execute('SELECT * FROM prueba WHERE usuario=? AND contraseña=?', (usuario, contraseña))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")

            def aceptar():
                    
                    nombre = entry_nombre.get()
                    codigo = entry_codigo.get()
                    valor = entry_valor.get()
                    unidad = entry_unidad.get()

                    if nombre and codigo and valor and unidad:
                        try:
                            
                            connection = sqlite3.connect("Base_de_prueba.db")
                            cursor = connection.cursor()

                            cursor.execute('''
                                CREATE TABLE IF NOT EXISTS reutilizable (
                                    Nombre TEXT NOT NULL,
                                    Código TEXT NOT NULL,
                                    Valor TEXT NOT NULL,
                                    Unidad TEXT NOT NULL           
                              ) 
                          ''')
                            cursor.execute("INSERT INTO reutilizable (Nombre, Código, Valor, Unidad) VALUES (?, ?, ?, ?)",
                                           (nombre, codigo, valor, unidad))
                            connection.commit()
                            messagebox.showinfo("Ventana de Facturación", "Datos insertados con éxito en la base de datos.")

                        except sqlite3.Error as e:
                            print("Error de SQLite:", e)
                            messagebox.showerror("Error de Facturación", "No se pudo insertar los datos en la base de datos.")
                        finally:

                            connection.close()

                            entry_nombre.delete(0, tk.END)
                            entry_codigo.delete(0, tk.END)
                            entry_valor.delete(0, tk.END)
                            entry_unidad.delete(0, tk.END)
                    else:
                        messagebox.showerror("Error de Facturación", "No se pudo insertar los datos en la base de datos.")
            def imprimir():
                try:
                    p = Network("192.168.20.52", 9100) 
                    p.text(resultado_text.get(1.0, tk.END))  
                    p.cut()
                except Exception as e:
                    print(f"Error de Impresión: {str(e)}")
                    messagebox.showerror("Error de Impresión", f"No se pudo imprimir: {str(e)}")

            
            def mostrar_factura():
                try:
                    connection = sqlite3.connect("Base_de_prueba.db")
                    cursor = connection.cursor()
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS reutilizable (
                            Nombre TEXT NOT NULL,
                            Código TEXT NOT NULL,
                            Valor TEXT NOT NULL,
                            Unidad TEXT NOT NULL           
                        ) 
                    ''')
                    cursor.execute('SELECT * FROM reutilizable')
                    productos = cursor.fetchall()
                    if productos:
                        resultado_text.config(state=tk.NORMAL)
                        resultado_text.delete(1.0, tk.END)
                        resultado_text.insert(tk.END, "**************************************************\n")
                        resultado_text.insert(tk.END, "********************** Factura *******************\n")
                        resultado_text.insert(tk.END, "**************************************************\n\n")
                        for producto in productos:
                            nombre = producto[0]
                            codigo = producto[1]
                            valor = producto[2]
                            unidad = producto[3]
                            resultado_text.insert(tk.END, f"{nombre} ({codigo}) - Unidad: {unidad} - Valor: {valor}\n")
                            
                        total = sum(int(producto[2]) for producto in productos)
                        resultado_text.insert(tk.END, "\n*******************\n")
                        resultado_text.insert(tk.END, f"Total: ${total}\n")
                        resultado_text.insert(tk.END, "*******************\n")
                            
                        resultado_text.config(state=tk.DISABLED)
                    else:
                        messagebox.showinfo("Factura Vacía", "No se han ingresado productos. La factura está vacía.")
                except sqlite3.Error as e:
                    print("Error de SQLite:", e)
                    messagebox.showerror("Error de Facturación", "No se pudo obtener la factura desde la base de datos.")
                finally:
                    connection.close()
                           
            def Borrar_factura():
                try:
                    conexion = sqlite3.connect("Base_de_prueba.db")
                    cursor = conexion.cursor()
                    reutilizable = "reutilizable"
                    consulta = f"DELETE FROM {reutilizable};"
                    cursor.execute(consulta)
                    conexion.commit()
                    print(f"Contenido de la tabla {reutilizable} borrado exitosamente.")
                except sqlite3.Error as error:
                    print("Error al borrar el contenido de la tabla:", error)
                finally:
                    if conexion:
                        conexion.close()
                

            ventana_facturacion = tk.Toplevel(window)

            ventana_facturacion.title("Ventana de facturación")

            ancho_ventana_registro = 775
            altura_ventana_registro = 510

            ancho_pantalla = ventana_facturacion.winfo_screenwidth()
            altura_pantalla = ventana_facturacion.winfo_screenheight()

            x = (ancho_pantalla - ancho_ventana_registro) // 2
            y = (altura_pantalla - altura_ventana_registro) // 2
            
            ventana_facturacion.geometry(f"{ancho_ventana_registro}x{altura_ventana_registro}+{x}+{y}")

            label_text_0 = tk.Label(ventana_facturacion, text=" Sistema De Facturación ", font=("Times New Roman", 25))
            label_text_0.place(x=230, y=0)

            label_text_1 = tk.Label(ventana_facturacion, text=" Ingresa el nombre del Producto: ", font=("Times New Roman", 15))
            label_text_1.place(x=0, y=50)

            entry_nombre = tk.Entry(ventana_facturacion, width=50)
            entry_nombre.place(x=270, y=55)

            label_text_2 = tk.Label(ventana_facturacion, text=" Ingrese el código del producto: ", font=("Times New Roman", 15))
            label_text_2.place(x=0, y=85)

            entry_codigo = tk.Entry(ventana_facturacion, width=50)
            entry_codigo.place(x=270, y=90)  

            label_text_3 = tk.Label(ventana_facturacion, text=" Ingresa el valor del Producto: ", font=("Times New Roman", 15))
            label_text_3.place(x=0, y=120)

            entry_valor= tk.Entry(ventana_facturacion, width=50)
            entry_valor.place(x=270, y=125)  

            label_text_4 = tk.Label(ventana_facturacion, text=" Ingresa la unidad comprada del Producto: ", font=("Times New Roman", 15))
            label_text_4.place(x=0, y=150)

            entry_unidad = tk.Entry(ventana_facturacion, width=50)
            entry_unidad.place(x=350, y=155)  

            Button_imprimir = tk.Button(ventana_facturacion, text=("Imprimir"), command=imprimir)
            Button_imprimir.place(x=700, y=400)

            Button_Aceptar = tk.Button(ventana_facturacion, text=("Aceptar"), command=aceptar)
            Button_Aceptar.place(x=630, y=400)

            Button_mostrar_factura = tk.Button(ventana_facturacion, text=("mostrar factura"), command=mostrar_factura)
            Button_mostrar_factura.place(x=520, y=400)
            
            Button_Borrar_factura = tk.Button(ventana_facturacion, text=("Borrar factura "), command=Borrar_factura)
            Button_Borrar_factura.place(x=420, y=400)

            resultado_text = tk.Text(ventana_facturacion, height=15, width=50, state=tk.DISABLED)
            resultado_text.place(x=0, y=200)

            ventana_facturacion.mainloop()           

        else:
            messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas")

    except sqlite3.Error as e:
        print("Error de SQLite:", e)

    finally:
        connection.close()

           
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

    label_texto = tk.Label(ventana_registro, text=" Registro ", font=("Times New Roman", 20))
    label_texto.place(x=120, y=0)

    label_usuario = tk.Label(ventana_registro, text=" Usuario ", font=("Times New Roman", 20))
    label_usuario.place(x=15, y=45)
    entry_usuario_reg = tk.Entry(ventana_registro)
    entry_usuario_reg.place(x=25, y=80)

    label_contraseña = tk.Label(ventana_registro, text=" Contraseña ", font=("Times New Roman", 20))
    label_contraseña.place(x=15, y=120)
    entry_contraseña_reg = tk.Entry(ventana_registro, show="*")
    entry_contraseña_reg.place(x=25, y=160)

    boton_registrar = tk.Button(ventana_registro, text="Registrar", command=lambda: mensaje_registro(entry_usuario_reg.get(), entry_contraseña_reg.get()))
    boton_registrar.place(x=275, y=200)

def mensaje_registro(usuario_reg, contraseña_reg):

    connection = sqlite3.connect("Base_de_prueba.db")
    cursor = connection.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prueba (
                usuario TEXT,
                contraseña TEXT
            )
        ''')

        cursor.execute('INSERT INTO prueba (usuario, contraseña) VALUES (?, ?)', (usuario_reg, contraseña_reg))
        connection.commit()
        messagebox.showinfo("Ventana de Registro", "¡Usuario registrado con éxito!")
    except sqlite3.Error as e:
        print("Error de SQLite:", e)
        messagebox.showerror("Error de Registro", f"No se pudo registrar el usuario.")
    finally:
        connection.close()
  
window = tk.Tk()

window.title(" Sistema de facturacion ")

ancho_ventana = 750
altura_ventana = 500

ancho_pantalla = window.winfo_screenwidth()
altura_pantalla = window.winfo_screenheight()

x = (ancho_pantalla - window.winfo_reqwidth()) // 3
y = (altura_pantalla - window.winfo_reqheight()) // 3

window.geometry("{}x{}+{}+{}".format(ancho_ventana, altura_ventana, x, y))

label_1 = tk.Label(window, text=" Sistema De Facturacion ", font=("Times New Roman", 25) )
label_1.place(x=220 , y=0)

label_usuario = tk.Label(window, text=" Usuario ", font=("Times New Roman", 20) )
label_usuario.place(x=300, y=85)
entry_usuario = tk.Entry(window)
entry_usuario.place(x=310, y=130)

label_contraseña = tk.Label(window, text=" Contraseña ", font=("Times New Roman", 20) )
label_contraseña.place(x=300, y=175)
entry_contraseña = tk.Entry(window, show="*")
entry_contraseña.place(x=310, y=220)

button = tk.Button(window, text="Iniciar sesion ",command= inicio_sesion)
button.place(x=375, y=300)


button = tk.Button(window, text=" registrarte ", command=registro)
button.place(x=280, y=300)


window.mainloop()
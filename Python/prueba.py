import tkinter as tk
from tkinter import messagebox

productos = []
factura = []

def agregar_producto():
    codigo = entry_codigo.get()
    producto = entry_nombre.get()
    valor_producto = entry_valor.get()
    producto_unidad = entry_unidad.get()

    if not (codigo and producto and valor_producto and producto_unidad):
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    productos.append({"nombre": producto, "valor_producto": int(valor_producto)})
    factura.append({"nombre": producto, "producto_unidad": int(producto_unidad), "subtotal": int(valor_producto) * int(producto_unidad)})

    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_unidad.delete(0, tk.END)

def mostrar_factura():
    if factura:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "*****************************\n")
        resultado_text.insert(tk.END, "********** Factura **********\n")
        resultado_text.insert(tk.END, "*****************************\n\n")

        for item in factura:
            resultado_text.insert(tk.END, f"{item['nombre']} x{item['producto_unidad']}: ${item['subtotal']}\n")

        total = sum(item['subtotal'] for item in factura)
        resultado_text.insert(tk.END, "\n*******************\n")
        resultado_text.insert(tk.END, f"Total: ${total}\n")
        resultado_text.insert(tk.END, "*******************\n")
        resultado_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Factura Vacía", "No se han ingresado productos. La factura está vacía.")

# Crear la ventana principal
window = tk.Tk()
window.title("Sistema de Facturación")

# Crear campos de entrada
entry_codigo = tk.Entry(window, width=30)
entry_nombre = tk.Entry(window, width=30)
entry_valor = tk.Entry(window, width=30)
entry_unidad = tk.Entry(window, width=30)

# Crear etiquetas
label_codigo = tk.Label(window, text="Código del Producto:")
label_nombre = tk.Label(window, text="Nombre del Producto:")
label_valor = tk.Label(window, text="Valor del Producto:")
label_unidad = tk.Label(window, text="Unidad Comprada:")

# Crear botones
Button_Agregar = tk.Button(window, text="Agregar Producto", command=agregar_producto)
Button_MostrarFactura = tk.Button(window, text="Mostrar Factura", command=mostrar_factura)

# Crear un área de texto para mostrar la factura
resultado_text = tk.Text(window, height=15, width=50, state=tk.DISABLED)

# Posicionar elementos en la ventana principal
label_codigo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_codigo.grid(row=0, column=1, padx=10, pady=5)
label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)
label_valor.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_valor.grid(row=2, column=1, padx=10, pady=5)
label_unidad.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_unidad.grid(row=3, column=1, padx=10, pady=5)
Button_Agregar.grid(row=4, column=0, columnspan=2, pady=10)
Button_MostrarFactura.grid(row=5, column=0, columnspan=2, pady=10)
resultado_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
window.mainloop()


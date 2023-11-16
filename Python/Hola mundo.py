import tkinter as tk

def robar_teclado():
    label.config(text="HOLA MUNDO")

window = tk.Tk()
window.geometry("500x250")

label = tk.Label(window, text="Presiona el botón ", font=("Arial", 14))
label.pack(pady=20)


button = tk.Button(window, text="has click", command=robar_teclado)
button.pack()

window.mainloop()

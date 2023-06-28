
import random
import string
import tkinter as tk

def generar_palabra(proveedor):
    palabra = ""
    for i in range(9):
        if i % 3 == 2:
            palabra += str(random.randint(1, 9))
        else:
            palabra += random.choice(string.ascii_lowercase)
    return palabra + "@" + proveedor

"""

def generar_correos():
    proveedor = variable_proveedor.get()
    cantidad = int(variable_cantidad.get())
    for i in range(cantidad):
        print(generar_palabra(proveedor))

root = tk.Tk()

variable_proveedor = tk.StringVar(root)
variable_proveedor.set("mailbox.org")

opciones_proveedor = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.es", "protonmail.com", "aolmail.com", "zoho.com", "icloud.com", "gmx.com", "mail.com", "mailbox.org", "tutanota.com"]
menu_proveedor = tk.OptionMenu(root, variable_proveedor, *opciones_proveedor)
menu_proveedor.pack()

variable_cantidad = tk.StringVar(root)
variable_cantidad.set("5")

entrada_cantidad = tk.Entry(root, textvariable=variable_cantidad)
entrada_cantidad.pack()

boton_generar = tk.Button(root, text="Generar correos electrónicos", command=generar_correos)
boton_generar.pack()

root.mainloop()

"""

def generar_correos():
    proveedor = variable_proveedor.get()
    cantidad = int(variable_cantidad.get())
    correos = []
    for i in range(cantidad):
        correos.append(generar_palabra(proveedor))
    texto_correos.delete("1.0", tk.END)
    texto_correos.insert(tk.END, "\n".join(correos))

root = tk.Tk()

variable_proveedor = tk.StringVar(root)
variable_proveedor.set("mailbox.org")

opciones_proveedor = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.es", "protonmail.com", "aolmail.com", "zoho.com", "icloud.com", "gmx.com", "mail.com", "mailbox.org", "tutanota.com"]
menu_proveedor = tk.OptionMenu(root, variable_proveedor, *opciones_proveedor)
menu_proveedor.pack()

variable_cantidad = tk.StringVar(root)
variable_cantidad.set("5")

entrada_cantidad = tk.Entry(root, textvariable=variable_cantidad)
entrada_cantidad.pack()

boton_generar = tk.Button(root, text="Generar correos electrónicos", command=generar_correos)
boton_generar.pack()

texto_correos = tk.Text(root)
texto_correos.pack()

root.mainloop()


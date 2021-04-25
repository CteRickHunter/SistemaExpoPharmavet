from tkinter import *
import subprocess



# Configuración de la raíz
color="#DAA520"

root = Tk()

root.title("Sistema Documental de Exportaciones Pharmavet")
root.iconbitmap("images/logo.ico")
root.config(bg=color, width="1050", height="700")
root.eval('tk::PlaceWindow . center')
root.resizable(0,0)

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Paises",command=lambda:subprocess.run(["python","view_paises.py"]))
filemenu.add_command(label="Clientes",command=lambda:subprocess.run(["python","view_clientes.py"]))
filemenu.add_command(label="Precios",command=lambda:subprocess.run(["python","view_pais_precio.py"]))
filemenu.add_command(label="Productos",command=lambda:subprocess.run(["python","view_productos.py"]))
filemenu.add_command(label="Lotes",command=lambda:subprocess.run(["python","view_lotes.py"]))
filemenu.add_command(label="SENASA",command=lambda:subprocess.run(["python","view_datos_SENASA.py"]))
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

pedidomenu = Menu(menubar, tearoff=0)
pedidomenu.add_command(label="Ingreso",command=lambda:subprocess.run(["python","view_pedidos.py"]))
pedidomenu.add_command(label="Modificar")
pedidomenu.add_command(label="Imprime",command=lambda:subprocess.run(["python","view_muestra_pedido.py"]))


listmenu = Menu(menubar, tearoff=0)
listmenu.add_command(label="Pedidos")
listmenu.add_command(label="Listado Empaque")
listmenu.add_command(label="Autorización SENASA")
listmenu.add_command(label="Listado Productos",command=lambda:subprocess.run(["python","view_productos_listado.py"]))
listmenu.add_command(label="Lista de Precios",command=lambda:subprocess.run(["python","view_pais_precio_listado.py"]))


menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Pedidos", menu=pedidomenu)
menubar.add_cascade(label="Listados", menu=listmenu)

# Finalmente bucle de la aplicación
root.mainloop()
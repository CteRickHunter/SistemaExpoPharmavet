# Programa para carga de datos en BBDD SQLite
import os
from tkinter import *

def cargaProd():
    
    os.system("carga_productos.py")
    
    

raiz=Tk()
raiz.title("Carga de Datos")
raiz.iconbitmap("images/logo.ico")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

# - - - - -  Titulos del menú - - - - - - 
menuCargar=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Cargar", menu=menuCargar)

# - - - - -  Submenues - - - - - - - - 
menuCargar.add_command(label="carga Productos", command=cargaProd)
menuCargar.add_command(label="carga Lotes")
menuCargar.add_command(label="carga Paises")
menuCargar.add_command(label="carga Datos_SENASA")


frame=Frame(raiz)
frame.config(bg="#f2d05e", width="650", height="350")
frame.pack(fill="both", expand="True")






raiz.mainloop()




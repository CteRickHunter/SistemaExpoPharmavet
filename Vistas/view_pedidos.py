# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Clases import Clientes, Pedidos


color="#f2d05e"



# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Pedidos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

dato_p=Pedidos.Pedidos()

dato_p.guardar_pedidos()
    
raiz.mainloop()




    














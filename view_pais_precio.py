# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Clases import Productos,Paises, Pais_Precios

color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarPrecio(cod_pais,cod_prod,precio):
    

    # - - - Control Datos -----
    f=True
    if len(cod_pais)>2:
        cod_pais=cod_pais[0:2]

    if cod_pais=="" or len(cod_pais)<2:
        messagebox.showerror("ERROR", "Cantidad del <<<Código de Pais>>>\n deben ser 2 caracteres")
        return
        f=False
    
    if len(cod_prod)>10:
        cod_prod=cod_prod[0:10]
        

    if cod_prod=="" or len(cod_prod)!=10:
        if len(cod_prod)!=10:
            messagebox.showerror("ERROR", "Cantidad del <<<Código de Producto>>>\n deben ser 10 caracteres")
            return
        f=False
    
    if float(precio)<0.01:
        messagebox.showerror("ERROR", "El <<<Precio>>>\n deben ser positivo")
        return
        f=False
    
    
    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    
    dato_p=Pais_Precios.Pais_Precios()
    dato_p.setear_precio(cod_pais,cod_prod,precio)
    dato_p.guardar_precio()

    
    limpiaDatos()

def limpiaDatos() :
    codigoProdEntry.set("")
    precio.set("")
    if not bool_var.get():
        codigoPaisEntry.set("")
        codigoPaisEntry.focus()
    else:
        codigoProdEntry.focus()
    


# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Precios x Pais")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")


precio=StringVar()
    
# - - - - -  Labels - - - - - -
codigoPaisLbl=Label(frame,text="Código Pais: ")
codigoPaisLbl.config(bg=color)
codigoPaisLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)


codigoProdLbl=Label(frame,text="Código Producto: ")
codigoProdLbl.config(bg=color)
codigoProdLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

precioLbl=Label(frame,text="Precio del Producto: ")
precioLbl.config(bg=color)
precioLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)


# - - - - - Entrys - - - - - - 

lista=[]
lista_pais=Paises.Paises()
lista=lista_pais.leer_lista(lista)
codigoPaisEntry=ttk.Combobox(frame,values=lista,width=40,state="readonly")
codigoPaisEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5)
codigoPaisEntry.config(font="Arial 10")

bool_var = BooleanVar()
fijoCheck=ttk.Checkbutton(frame,text="Fijar",variable=bool_var)
fijoCheck.grid(row=0,column=2)

lista2=[]
lista_prod=Productos.Productos()
lista2=lista_prod.leer_lista()
codigoProdEntry=ttk.Combobox(frame,values=lista2,width=40,state="readonly")
codigoProdEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
codigoProdEntry.config(font="Arial 10")

precioEntry=Entry(frame,textvariable=precio,width=10)
precioEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
precioEntry.config(font="Arial 15")


guardarBtn=Button(frame,text="Guardar", command=lambda:grabarPrecio(codigoPaisEntry.get(),codigoProdEntry.get(),precio.get()))
guardarBtn.grid(row=5,column=0,columnspan=2,ipady=5, pady=5)
guardarBtn.config(width="60")

limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=6,column=0,columnspan=2,ipady=5, pady=5)
limpiarBtn.config(width="60")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=7,column=0,columnspan=2,ipady=5, pady=5)
salirBtn.config(width="60")

codigoProdEntry.focus()
    
raiz.mainloop()

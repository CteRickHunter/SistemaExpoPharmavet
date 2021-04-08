# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Clases import Pedidos,Clientes, Paises



color="#f2d05e"
# - - - - - - - funciones - - - - - - - - 

def grabarPed(cod):
    
    pass

def limpiar_cliente():
    codigoCliEntry.set("")
    nombre.set("")
    localidad.set("")
    nom_pais.set("")    
    incotermEntry.set("")
    condicionEntry.set("")
    codigoCliEntry.focus()

def confirma_cliente(cod):
    if len(cod)>6:
        cod=cod[0:6]
        codigoCliEntry.set(cod)


    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
             messagebox.showerror("ERROR", "Código de cliente está errado")
             return
        f=False
    
    messagebox.showinfo("CORRECTO", "Todo bien")
    cli=Clientes.Clientes()
    
    cli.buscar_cliente(cod)
    pais=Paises.Paises()
    nombre_pais=pais.busca_nombre(cli.cod_pais)

    nombre.set(cli.nombre)
    localidad.set(cli.localidad)
    nom_pais.set(nombre_pais)

    confirmaBtn.focus()
    

    

# - - - - - - - - - - Prog. Principal - - - - - - - 
raiz=Tk()
raiz.title("Carga de Pedidos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")
# - - - - - -  Variables para los Entry - - - - - -

nombre = StringVar()
localidad = StringVar()
nom_pais = StringVar()
incoterm = StringVar()




# - - - - -  Labels - - - - - -
pedidosLbl=Label(frame,text="Pedidos")
pedidosLbl.config(bg=color,font="Arial 25")
pedidosLbl.grid(row=0,column=0,padx=5, pady=5, columnspan=5)

codigoCliLbl=Label(frame,text="Código Cliente: ")
codigoCliLbl.config(bg=color)
codigoCliLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

nombreLbl=Label(frame,text="Nombre: ")
nombreLbl.config(bg=color)
nombreLbl.grid(row=1,column=2,sticky="e",padx=5, pady=5)

localidadLbl=Label(frame,text="Localidad: ")
localidadLbl.config(bg=color)
localidadLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

nomPaisLbl=Label(frame,text="País: ")
nomPaisLbl.config(bg=color)
nomPaisLbl.grid(row=2,column=2,sticky="e",padx=5, pady=5)

incotermLbl=Label(frame,text="INCOTERM: ")
incotermLbl.config(bg=color)
incotermLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

notaLbl=Label(frame,text="Condición\n de Venta: ")
notaLbl.config(bg=color)
notaLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

pedidoLbl=Label(frame,text="Pedido: ")
pedidoLbl.config(bg=color)
pedidoLbl.grid(row=6,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
lista=[]
lista_clientes=Clientes.Clientes()
lista=lista_clientes.leer_lista(lista)
codigoCliEntry=ttk.Combobox(frame,values=lista,width=30,state="readonly")
codigoCliEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
codigoCliEntry.config(font="Arial 10")


nombreEntry=Entry(frame,textvariable=nombre,width=30,state="readonly")
nombreEntry.grid(row=1,column=3,sticky="w",padx=5, pady=5, columnspan=2)
nombreEntry.config(font="Arial 15")


localidadEntry=Entry(frame,textvariable=localidad,state="readonly")
localidadEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
localidadEntry.config(font="Arial 15")


nomPaisEntry=Entry(frame,textvariable=nom_pais,width=30,state="readonly")
nomPaisEntry.grid(row=2,column=3,sticky="w",padx=5, pady=5)
nomPaisEntry.config(font="Arial 10")


incoterms=[
    "FOB-Rosario-Santa FE-ARG", 
    "FOB-Buenos Aires-ARG","CIF-Destino"]
incotermEntry=ttk.Combobox(frame,values=incoterms,width=30,state="readonly")
incotermEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,)
incotermEntry.config(font="Arial 12")

condiciones=[
    "100% Adelantado", 
    "50% Adelantado, 50% a 30 días F.Emb.",
    "A 60 días F.Embarque",
    "A 90 días F. Embarque"]
condicionEntry=ttk.Combobox(frame,values=condiciones,width=30,state="readonly")
condicionEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5,)
condicionEntry.config(font="Arial 12")



confirmaBtn=Button(frame,text="Confirma Cliente", command=lambda:confirma_cliente(codigoCliEntry.get()))
confirmaBtn.grid(row=5,column=1,ipady=5)
confirmaBtn.config(width="40")

limpiaBtn=Button(frame,text="Limpiar Datos", command=lambda:limpiar_cliente())
limpiaBtn.grid(row=5,column=2,ipady=5)
limpiaBtn.config(width="40")

pedidoEntry=Text(frame,width=60, height=10)
pedidoEntry.grid(row=6,column=1,sticky="w",padx=5, pady=5, columnspan=2,rowspan=4)
pedidoEntry.config(font="Arial 12")

nuevoItemBtn=Button(frame,text="Nuevo Item", command=lambda:grabarPed(codigoCliEntry.get()))
nuevoItemBtn.grid(row=6,column=4,ipady=5)
nuevoItemBtn.config(width="20")

grabarPedBtn=Button(frame,text="Confirma Cliente", command=lambda:grabarPed(codigoCliEntry.get()))
grabarPedBtn.grid(row=7,column=4,ipady=5)
grabarPedBtn.config(width="20")

#limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
#limpiarBtn.grid(row=10,column=0,columnspan=2,ipady=5)
#limpiarBtn.config(width="60")


#salirBtn=Button(frame,text="Salir",command=raiz.destroy)
#salirBtn.grid(row=11,column=0,columnspan=2,ipady=5)
#salirBtn.config(width="60")

codigoCliEntry.focus()
    
raiz.mainloop()

#dato_p=Pedidos.Pedidos()

#dato_p.guardar_pedidos()
    





    














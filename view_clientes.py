# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Clases import Clientes, Paises


color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarCli(cod,nom,dir,loc,pais,cod_trib,cond,tel,mail):
    

    # - - - Control Datos -----
    f=True
    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
             messagebox.showerror("ERROR", "Cantidad del <<<Código Cliente>>>\n deben ser 6 caracteres")
             return
        f=False
    
        
    if nom=="":
        f=False

    if dir=="":
        f=False

    if loc=="":
        f=False
    
    if len(pais)>2:
        pais=pais[0:2]

    if pais=="" or len(pais)!=2:
        if len(pais)!=2:
             messagebox.showerror("ERROR", "Cantidad del <<<Código País>>>\n deben ser 2 caracteres")
             return
        f=False
    
    if cod_trib=="":
        f=False

    
    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    

    conectado=sqlite3.connect("SistemaExpo")
    puntero=conectado.cursor()
    
    puntero.execute("INSERT INTO Clientes VALUES('"+cod+"','"+nom+"','"+dir+"','"+loc+"','"+pais+"','"+cod_trib+"','"+cond+"','"+tel+"','"+mail+"')")
    
    conectado.commit()
    conectado.close()
    limpiaDatos()

def limpiaDatos() :
    cod_cliente.set("")
    nombre.set("")
    direccion.set("")
    localidad.set("")
    codPaisEntry.set("")
    id_tributaria.set("")
    condicion_venta.set("")
    telefono.set("")
    correo_electronico.set("")
    codigoCliEntry.focus()
    


# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Clientes")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

cod_cliente = StringVar()
nombre = StringVar()
direccion = StringVar()
localidad = StringVar()
#cod_pais = StringVar()
id_tributaria = StringVar()
condicion_venta = StringVar()
telefono = StringVar()
correo_electronico = StringVar()

    
# - - - - -  Labels - - - - - -
codigoCliLbl=Label(frame,text="Código Cliente: ")
codigoCliLbl.config(bg=color)
codigoCliLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)

nombreLbl=Label(frame,text="Nombre: ")
nombreLbl.config(bg=color)
nombreLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

direccionLbl=Label(frame,text="Dirección: ")
direccionLbl.config(bg=color)
direccionLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

localidadLbl=Label(frame,text="Localidad: ")
localidadLbl.config(bg=color)
localidadLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

codPaisLbl=Label(frame,text="Código del País: ")
codPaisLbl.config(bg=color)
codPaisLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

idTributariaLbl=Label(frame,text="Identificación Tributaria: ")
idTributariaLbl.config(bg=color)
idTributariaLbl.grid(row=5,column=0,sticky="e",padx=5, pady=5)

condicionVtaLbl=Label(frame,text="Condición de Venta: ")
condicionVtaLbl.config(bg=color)
condicionVtaLbl.grid(row=6,column=0,sticky="e",padx=5, pady=5)

telefonoLbl=Label(frame,text="Teléfono: ")
telefonoLbl.config(bg=color)
telefonoLbl.grid(row=7,column=0,sticky="e",padx=5, pady=5)

correoLbl=Label(frame,text="correo electrónico: ")
correoLbl.config(bg=color)
correoLbl.grid(row=8,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
codigoCliEntry=Entry(frame,textvariable=cod_cliente,width=6)
codigoCliEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5,ipady=5)
codigoCliEntry.config(font="Arial 15")

nombreEntry=Entry(frame,textvariable=nombre)
nombreEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
nombreEntry.config(font="Arial 15")

direccionEntry=Entry(frame,textvariable=direccion)
direccionEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
direccionEntry.config(font="Arial 15")

localidadEntry=Entry(frame,textvariable=localidad)
localidadEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,)
localidadEntry.config(font="Arial 15")


lista=[]
lista_paises=Paises.Paises()
lista=lista_paises.leer_lista(lista)
codPaisEntry=ttk.Combobox(frame,values=lista,width=30)
codPaisEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5)
codPaisEntry.config(font="Arial 10")

idTributariaEntry=Entry(frame,textvariable=id_tributaria)
idTributariaEntry.grid(row=5,column=1,sticky="w",padx=5, pady=5,)
idTributariaEntry.config(font="Arial 15")

condicionVtaEntry=Entry(frame,textvariable=condicion_venta)
condicionVtaEntry.grid(row=6,column=1,sticky="w",padx=5, pady=5,)
condicionVtaEntry.config(font="Arial 15")

telefonoEntry=Entry(frame,textvariable=telefono)
telefonoEntry.grid(row=7,column=1,sticky="w",padx=5, pady=5,)
telefonoEntry.config(font="Arial 15")

mailEntry=Entry(frame,textvariable=correo_electronico)
mailEntry.grid(row=8,column=1,sticky="w",padx=5, pady=5,)
mailEntry.config(font="Arial 15")

guardarBtn=Button(frame,text="Guardar", command=lambda:grabarCli(cod_cliente.get(),nombre.get(),direccion.get(),localidad.get(),codPaisEntry.get(),id_tributaria.get(),condicion_venta.get(),telefono.get(),correo_electronico.get()))
guardarBtn.grid(row=9,column=0,columnspan=2,ipady=5)
guardarBtn.config(width="60")

limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=10,column=0,columnspan=2,ipady=5)
limpiarBtn.config(width="60")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=11,column=0,columnspan=2,ipady=5)
salirBtn.config(width="60")

codigoCliEntry.focus()
    
raiz.mainloop()




    














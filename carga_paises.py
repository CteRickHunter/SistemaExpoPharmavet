# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox


color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarPais(cod,pais,cuit):
    

    # - - - Control Datos -----
    f=True
    if cod=="" or len(cod)!=2:
        if len(cod)!=2:
             messagebox.showerror("ERROR", "Cantidad del <<<Código del País>>>\n deben ser 2 caracteres")
             return
        f=False
    
    cod=cod.upper()
       
    if pais=="":
        f=False
    
    if cuit=="" or len(cuit)!=11:
        if len(cuit)!=11:
             messagebox.showerror("ERROR", "Cantidad del <<<CUIT del País>>>\n deben ser 11 caracteres")
             return
        f=False
    
    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    

    conectado=sqlite3.connect("SistemaExpo")
    puntero=conectado.cursor()
    
    puntero.execute("INSERT INTO Paises VALUES('"+cod+"','"+pais+"','"+cuit+"')")
    
    conectado.commit()
    conectado.close()
    limpiaDatos()

def limpiaDatos() :
    cod.set("")
    pais.set("")
    cuit.set("")
    
    codigoEntry.focus()
    


# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Paises")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

cod = StringVar()
pais = StringVar()
cuit = StringVar()
    
# - - - - -  Labels - - - - - -
codigoLbl=Label(frame,text="Código País: ")
codigoLbl.config(bg=color)
codigoLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)

paisLbl=Label(frame,text="País: ")
paisLbl.config(bg=color)
paisLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

cuitLbl=Label(frame,text="CUIT del país: ")
cuitLbl.config(bg=color)
cuitLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
codigoEntry=Entry(frame,textvariable=cod,width=2)
codigoEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5,ipady=5)
codigoEntry.config(font="Arial 15")

paisEntry=Entry(frame,textvariable=pais)
paisEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
paisEntry.config(font="Arial 15")

cuitEntry=Entry(frame,textvariable=cuit,width=11)
cuitEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
cuitEntry.config(font="Arial 15")

guardarBtn=Button(frame,text="Guardar", command=lambda:grabarPais(cod.get(),pais.get(),cuit.get()))
guardarBtn.grid(row=3,column=0,columnspan=2,ipady=5)
guardarBtn.config(width="60")

limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=4,column=0,columnspan=2,ipady=5)
limpiarBtn.config(width="60")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=5,column=0,columnspan=2,ipady=5)
salirBtn.config(width="60")

codigoEntry.focus()
    
raiz.mainloop()




    














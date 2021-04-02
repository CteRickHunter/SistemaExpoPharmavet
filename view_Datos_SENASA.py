# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox

from Clases import Senasa

color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarDatosSenasa(cod,nom,nroexp,nrocer,nmn):
    

    # - - - Control Datos -----
    f=True
    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
             messagebox.showerror("ERROR", "Cantidad del <<<Código Producto SENASA>>>\n deben ser 6 caracteres")
             return
        f=False
           
    if nom=="":
        f=False
    
    if nroexp=="":
        f=False
    
    if nrocer=="":
        f=False

    if nmn=="" or len(nmn)!=15:
        if len(nmn)!=15:
             messagebox.showerror("ERROR", "Cantidad del <<<Nomenclador MERCOSUR>>>\n deben ser 15 caracteres")
             return
        f=False

    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    

    #conectado=sqlite3.connect("SistemaExpo")
    #puntero=conectado.cursor()
    
    dato_s=Senasa.Senasa()
    dato_s.setear_senasa(cod,nom,nroexp,nrocer,nmn)
    dato_s.guardar_senasa()


    #puntero.execute("INSERT INTO Datos_SENASA VALUES('"+cod+"','"+nom+"','"+nroexp+"','"+nrocer+"','"+nmn+"')")
    
    #conectado.commit()
    #conectado.close()
    limpiaDatos()

def limpiaDatos() :
    cod_producto_base.set("")
    nombre_producto.set("")
    nro_expediente.set("")
    nro_certificado.set("")
    nomenclador.set("")
    codigoProdEntry.focus()



# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Datos SENASA")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

cod_producto_base = StringVar()
nombre_producto = StringVar()
nro_expediente = StringVar()
nro_certificado = StringVar()
nomenclador = StringVar()

    
# - - - - -  Labels - - - - - -
codigoProdLbl=Label(frame,text="Código Producto SENASA: ")
codigoProdLbl.config(bg=color)
codigoProdLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)


nombreSENASALbl=Label(frame,text="Nombre Producto SENASA: ")
nombreSENASALbl.config(bg=color)
nombreSENASALbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

nroExpedienteLbl=Label(frame,text="Número de Expediente: ")
nroExpedienteLbl.config(bg=color)
nroExpedienteLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

nroCertificadoLbl=Label(frame,text="Número de Certificado: ")
nroCertificadoLbl.config(bg=color)
nroCertificadoLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

nomencladorLbl=Label(frame,text="Nomenclador MERCOSUR: ")
nomencladorLbl.config(bg=color)
nomencladorLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 

codigoProdEntry=Entry(frame,textvariable=cod_producto_base,width=6)
codigoProdEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5,ipady=5)
codigoProdEntry.config(font="Arial 15")

nombreSENASAEntry=Entry(frame,textvariable=nombre_producto)
nombreSENASAEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
nombreSENASAEntry.config(font="Arial 15")

nroExpedienteEntry=Entry(frame,textvariable=nro_expediente)
nroExpedienteEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
nroExpedienteEntry.config(font="Arial 15")

nroCertificadoEntry=Entry(frame,textvariable=nro_certificado)
nroCertificadoEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,)
nroCertificadoEntry.config(font="Arial 15")

nomencladorEntry=Entry(frame,textvariable=nomenclador,width=15)
nomencladorEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5)
nomencladorEntry.config(font="Arial 15")

guardarBtn=Button(frame,text="Guardar", command=lambda:grabarDatosSenasa(cod_producto_base.get(),nombre_producto.get(),nro_expediente.get(),nro_certificado.get(),nomenclador.get()))
guardarBtn.grid(row=5,column=0,columnspan=2,ipady=5)
guardarBtn.config(width="60")

limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=6,column=0,columnspan=2,ipady=5)
limpiarBtn.config(width="60")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=7,column=0,columnspan=2,ipady=5)
salirBtn.config(width="60")

codigoProdEntry.focus()
    
raiz.mainloop()




    














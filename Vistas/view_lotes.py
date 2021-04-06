# Programa para carga de datos en BBDD SQLite

#import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime as dt

#-- nuevo
from Clases import Lotes,Senasa

color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarLote(lote,elab,venc,cod):
    
    print(cod)
    
    # - - - Control Datos -----
    f=True
    if lote=="":
        f=False
           
    if elab=="" or len(elab)!=10:
        if len(elab)!=10:
            messagebox.showerror("ERROR", "Cantidad del <<<Fecha de Elaboración>>>\n deben ser 10 caracteres")
            return
        f=False
    if (verificaFechaErrada(elab)):
        messagebox.showerror("ERROR", "Está mal ingresada la Fecha de Elaboración")
        return
    
    if venc=="" or len(venc)!=10:
        if len(venc)!=10:
            messagebox.showerror("ERROR", "Cantidad del <<<Fecha de Vencimiento>>>\n deben ser 10 caracteres")
            return
        f=False
    if (verificaFechaErrada(venc)):
        messagebox.showerror("ERROR", "Está mal ingresada la Fecha de Vencimiento")
        return

    if (verificadiferenciaFecha(elab,venc)):
        messagebox.showerror("ERROR", "La año de Vencimiento debe ser posterior al año de Elaboración")
        return

    if len(cod)>6:
        cod=cod[0:6]

    print(cod)

    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
            messagebox.showerror("ERROR", "Cantidad del <<<Código Producto SENASA>>>\n deben ser 6 caracteres")
            return
        f=False
    
    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    
    #-- nuevo --
    #conectado=sqlite3.connect("SistemaExpo")
    #puntero=conectado.cursor()
    dato=Lotes.Lotes(lote,elab,venc,cod)
    dato.guardar_lote()
    
    #puntero.execute("INSERT INTO Lotes VALUES('"+lote+"','"+elab+"','"+venc+"','"+cod+"')")
    
    #conectado.commit()
    #conectado.close()
    limpiaDatos()

def limpiaDatos() :
    lote.set("")
    elab.set("")
    venc.set("")
    codEntry.set("")
    cod.set("")
    
    loteEntry.focus()
    
def verificaFechaErrada(fechaString):
    flag=False
    sep1=fechaString[2]
    sep2=fechaString[5]
    if (sep1!="/" and sep1!="-")or(sep2!="/" and sep2!="-"):
        flag=True
    mes=fechaString[3:5]
    if mes.isdigit():
        if int(mes)<1 or int(mes)>12:
            flag=True
    else:
        flag=True
    anio=fechaString[6:10]
    if anio.isdigit():
        if int(anio)<2021 or int(anio)>2040:
            flag=True
    else:
        flag=True
    bisiesto=[2024,2028,2032,2036,2040]
    dia=fechaString[0:2]
    
    if dia.isdigit():
        if int(dia)<1 or int(dia)>31:
            flag=True
        if (int(dia)==31) and (int(mes) in [2,4,6,9,11]):
            flag=True
        if (int(dia)==30) and (int(mes)==2):
            flag=True
        if (int(dia)==29) and (int(mes)==2) and (int(anio) not in bisiesto):
            flag=True
        
    else:
        flag=True

    #print(dia, mes,anio)

    return flag
def verificadiferenciaFecha(elab,venc):
    fecha_ant=elab[6:10]
    fecha_pos=venc[6:10]

    # True indica que esta mal
    if fecha_ant>fecha_pos:
        return True
    else:
        return False

def buscarProducto(cod):
    pass



# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga de Lotes")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

lote = StringVar()
elab = StringVar()
venc = StringVar()
cod = StringVar()
    
# - - - - -  Labels - - - - - -
loteLbl=Label(frame,text="Número Lote: ")
loteLbl.config(bg=color)
loteLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)

elabLbl=Label(frame,text="Fecha Elaboración: ")
elabLbl.config(bg=color)
elabLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

vencLbl=Label(frame,text="Fecha Vencimiento: ")
vencLbl.config(bg=color)
vencLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

codLbl=Label(frame,text="Código Producto SENASA: ")
codLbl.config(bg=color)
codLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
loteEntry=Entry(frame,textvariable=lote)
loteEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5,ipady=5)
loteEntry.config(font="Arial 15")

elabEntry=Entry(frame,textvariable=elab,width=10)
elabEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
elabEntry.config(font="Arial 15")

vencEntry=Entry(frame,textvariable=venc,width=10)
vencEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
vencEntry.config(font="Arial 15")


lista=[]
lista_senasa=Senasa.Senasa()
lista=lista_senasa.leer_lista(lista)
codEntry=ttk.Combobox(frame,values=lista,width=40)
codEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5)
codEntry.config(font="Arial 10")

guardarBtn=Button(frame,text="Guardar", command=lambda:grabarLote(lote.get(),elab.get(),venc.get(),codEntry.get()))
guardarBtn.grid(row=4,column=0,ipady=5,sticky="ew")
guardarBtn.config(width="30")

guardarBtn=Button(frame,text="Buscar", command=lambda:buscarProducto(cod.get()))
guardarBtn.grid(row=4,column=1,ipady=5,sticky="ew")
guardarBtn.config(width="30")


limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=5,column=0,columnspan=2,ipady=5)
limpiarBtn.config(width="63")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=6,column=0,columnspan=2,ipady=5)
salirBtn.config(width="63")

loteEntry.focus()
    
raiz.mainloop()




    














# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from Clases import Productos,Senasa

color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 

def grabarProd(cod1,cod2,nom,peso,vol):
    # Si ya existe registro, actualizar
    # caso contratio, ingresar

    # - - - Control Datos -----
    f=True
    if cod1=="" or len(cod1)!=10:
        if len(cod1)!=10:
             messagebox.showerror("ERROR", "Cantidad del <<<Código de Producto>>>\n deben ser 10 caracteres")
             return
        f=False
    
    if len(cod2)>6:
        cod2=cod2[0:6]
        codigoBaseEntry.set(cod2)

    if cod2=="" or len(cod2)!=6:
        if len(cod2)!=6:
             messagebox.showerror("ERROR", "Cantidad del <<<Código Base>>>\n deben ser 6 caracteres")
             return
        f=False
    
    if nom=="":
        f=False
    
    if peso=="":
        f=False
    
    if vol=="":
        f=False

    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    
    dato_p=Productos.Productos()
    dato_p.setear_producto(cod1,cod2,nom,peso,vol)
    if dato_p.existe_producto():
        # Actualizar
        dato_p.actualizar_producto()
    else:
        # Ingresar
        dato_p.guardar_producto()

    
    limpiaDatos()

def limpiaDatos() :
    codigo1.set("")
    codigoBaseEntry.set("")
    #codigo2.set("")
    nombre.set("")
    peso.set("")
    volumen.set("")
    codigoProdEntry.focus()
    
def buscarProducto():
    global hija
    prod=Productos.Productos()
    lista_productos=prod.leer_lista()

    hija=Toplevel()
    hija.title("Busca Producto")
    hija.iconbitmap("images/logo.ico")
    hija.resizable(0,0)

    frame2=Frame(hija)
    frame2.config(bg=color, width="650", height="350")
    frame2.pack(fill="both", expand="False")
    
    listaProdEntry=ttk.Combobox(frame2,values=lista_productos,width=40,state="readonly")
    listaProdEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
    listaProdEntry.config(font="Arial 10")

    
    eligeItemBtn=Button(frame2,text="Elige Producto", command=lambda:muestraProducto(listaProdEntry.get()))
    eligeItemBtn.grid(row=2,column=1,ipady=5)
    eligeItemBtn.config(width="20")

def muestraProducto(prod):
    global hija
    # Busca Producto y formatea
    cod=prod[0:10]
    p=Productos.Productos()
    p.busca_producto(cod)
    codigo1.set(p.cod_producto)
    codigoBaseEntry.set(p.cod_producto_base)
    nombre.set(p.nombre_producto)
    peso.set(p.peso_producto)
    volumen.set(p.volumen_producto)
    hija.destroy()

def listaProductos():

    global c, text
    pagina=1
           
    # Busco los productos e imprimo
    prod=Productos.Productos()
    
    nombre_archivo="Listado_Productos.pdf"
    c=canvas.Canvas(nombre_archivo, pagesize=A4)
    cabecera()

    lista=prod.listar_productos()
    renglon=0
    text.textLine(" Código    Producto                                                Peso    Vol.")
    text.textLine("")

    for li in lista:
        renglon=renglon+1
        
        text.textLine(li)

        if renglon==50:
            renglon=0
            pie(pagina)
            pagina+=1
            # nueva hoja
            cabecera()
            text.textLine(" Código    Producto                                                Peso    Vol.")
            text.textLine("")


    pie(pagina)
    c.save()
    


def cabecera():
     # Armo página
    global c, text
    
    c.rect(30,30,530,770)

    c.drawImage("./images/Logo-Pharmavet-300x127.jpg",50,750,width=75,height=30)
    
    text=c.beginText(210,750)
    text.setFont("Times-Roman",14)
    text.textLine("LISTADO DE PRODUCTOS: ")
    c.drawText(text)

    text=c.beginText(50,730)
    text.setFont("Courier",10)
    
    #lineas de separación
    c.line(30,730,560,730)
    text.textLine("")
    c.line(35,710,555,710)
    

def pie(pag):
    global c, text
    c.drawText(text)
    text=c.beginText(40,40)
    text.setFont("Times-Roman",8)
    text.textLine("Programado por: Osvaldo G. Campilongo                        página: "+str(pag))
    c.drawText(text)
    c.showPage()


    
    


# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Carga y Búsqueda de Productos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

codigo1 = StringVar()
#codigo2 = StringVar()
nombre = StringVar()
peso = StringVar()
volumen = StringVar()

    
# - - - - -  Labels - - - - - -
codigoProdLbl=Label(frame,text="Código Producto: ")
codigoProdLbl.config(bg=color)
codigoProdLbl.grid(row=0,column=0,sticky="e",padx=5, pady=5)


codigoBaseLbl=Label(frame,text="Código Base: ")
codigoBaseLbl.config(bg=color)
codigoBaseLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

nombreComercialLbl=Label(frame,text="Nombre del Producto: ")
nombreComercialLbl.config(bg=color)
nombreComercialLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

pesoProdLbl=Label(frame,text="Peso del Producto: ")
pesoProdLbl.config(bg=color)
pesoProdLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

volumenProdLbl=Label(frame,text="Volumen del Producto: ")
volumenProdLbl.config(bg=color)
volumenProdLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
codigoProdEntry=Entry(frame,textvariable=codigo1,width=10)
codigoProdEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5,ipady=5)
codigoProdEntry.config(font="Arial 15")


lista=[]
lista_senasa=Senasa.Senasa()
lista=lista_senasa.leer_lista(lista)
codigoBaseEntry=ttk.Combobox(frame,values=lista,width=40)
codigoBaseEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
codigoBaseEntry.config(font="Arial 10")

nombreComercialEntry=Entry(frame,textvariable=nombre,width=30)
nombreComercialEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5)
nombreComercialEntry.config(font="Arial 15")

pesoProdEntry=Entry(frame,textvariable=peso)
pesoProdEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,)
pesoProdEntry.config(font="Arial 15",width="10")

buscarBtn=Button(frame,text="Buscar", command=lambda:buscarProducto())
buscarBtn.grid(row=3,column=1,sticky="e",ipady=5, pady=5, padx=15)
buscarBtn.config(width="10")

volumenProdEntry=Entry(frame,textvariable=volumen)
volumenProdEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5)
volumenProdEntry.config(font="Arial 15",width="10")

listarBtn=Button(frame,text="Listar", command=lambda:listaProductos())
listarBtn.grid(row=4,column=1,sticky="e",ipady=5, pady=5, padx=15)
listarBtn.config(width="10")


guardarBtn=Button(frame,text="Guardar", command=lambda:grabarProd(codigo1.get(),codigoBaseEntry.get(),nombre.get(),peso.get(),volumen.get()))
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

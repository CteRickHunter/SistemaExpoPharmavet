# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

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
    
    if not precio.isdigit():
        messagebox.showerror("ERROR", "El <<<Precio>>>\n deben ser numérico")
        return


    if float(precio)<0.01:
        messagebox.showerror("ERROR", "El <<<Precio>>>\n deben ser positivo")
        return
    
    
    if(f==False):
        messagebox.showwarning("ERROR", "Faltó completar campos...")
        return
    
    dato_p=Pais_Precios.Pais_Precios()
    if dato_p.existe_precio(cod_pais,cod_prod):
        dato_p.cambia_precio(cod_pais,cod_prod,precio)
        
    else:    
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
    
def listaPrecios():
    global c, text
    pagina=1
    pais=codigoPaisEntry.get()
    if len(pais)>2:
        pais=pais[0:2]

    if pais=="" or len(pais)<2:
        messagebox.showerror("ERROR", "Cantidad del <<<Código de Pais>>>\n deben ser 2 caracteres")
        return

    # Busco datos del pais
    codigoPaisEntry.set(pais)
    el_pais=Paises.Paises()
    nombre_pais=el_pais.busca_nombre(pais)
    
    # Busco los precios de ese pais e imprimo
    prod=Productos.Productos()
    pre=Pais_Precios.Pais_Precios()
    lista=pre.lista_precios(pais)

    nombre_archivo="Listado.pdf"
    c=canvas.Canvas(nombre_archivo, pagesize=A4)
    cabecera(nombre_pais)

    renglon=0
    text.textLine("Producto                                                    Precio")
    text.textLine("")

    for li in lista:
        renglon=renglon+1
        cod_prod=li[0]
        precio_prod=li[1]
        prod.busca_producto(cod_prod)
        #print(prod.nombre_producto," precio: ",'{:.2f}'.format(precio_prod))
        n_p=prod.nombre_producto+"                                                "
        n_p=n_p[0:50]
        p_p='{:10.2f}'.format(precio_prod)

        text.textLine(n_p+"      "+p_p)

        if renglon==50:
            renglon=0
            pie(pagina)
            pagina+=1
            # nueva hoja
            cabecera(nombre_pais)
            text.textLine("Producto                                                    Precio")
            text.textLine("")


    pie(pagina)
    c.save()
    


def cabecera(nombre_pais):
     # Armo página
    global c, text
    
    c.rect(30,30,530,770)

    c.drawImage("./images/Logo-Pharmavet-300x127.jpg",50,750,width=75,height=30)
    
    text=c.beginText(210,750)
    text.setFont("Times-Roman",14)
    text.textLine("LISTADO DE PRECIOS: "+nombre_pais)
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
    

def buscarPrecio(pais,prod):
    if len(pais)>2:
        pais=pais[0:2]

    if pais=="" or len(pais)<2:
        messagebox.showerror("ERROR", "Cantidad del <<<Código de Pais>>>\n deben ser 2 caracteres")
        return
    
    if len(prod)>10:
        prod=prod[0:10]
        
    if prod=="" or len(prod)!=10:
        if len(prod)!=10:
            messagebox.showerror("ERROR", "Cantidad del <<<Código de Producto>>>\n deben ser 10 caracteres")
            return

    codigoProdEntry.set(prod)
    codigoPaisEntry.set(pais)

    print(pais, type(pais))
    print(prod, type(prod))

    tabla=Pais_Precios.Pais_Precios()
    valor=tabla.busca_precio(pais,prod)
    precio.set(valor)


# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Modifica y lista Precios x Pais")
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

buscarBtn=Button(frame,text="Buscar", command=lambda:buscarPrecio(codigoPaisEntry.get(),codigoProdEntry.get()))
buscarBtn.grid(row=2,column=1,sticky="e",ipady=5, pady=5)
buscarBtn.config(width="10")



guardarBtn=Button(frame,text="Guardar", command=lambda:grabarPrecio(codigoPaisEntry.get(),codigoProdEntry.get(),precio.get()))
guardarBtn.grid(row=5,column=0,columnspan=2,ipady=5, pady=5, padx=40)
guardarBtn.config(width="60")

limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=6,column=0,columnspan=2,ipady=5, pady=5)
limpiarBtn.config(width="60")

listarBtn=Button(frame,text="Listar Precios", command=lambda:listaPrecios())
listarBtn.grid(row=7,column=0,columnspan=2,ipady=5, pady=5)
listarBtn.config(width="60")

salirBtn=Button(frame,text="Salir", command=raiz.destroy)
salirBtn.grid(row=8,column=0,columnspan=2,ipady=5, pady=5)
salirBtn.config(width="60")

codigoProdEntry.focus()
    
raiz.mainloop()

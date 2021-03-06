# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

from Clases import Productos,Paises, Pais_Precios

color="#f2d05e"


# - - - - - - - funciones - - - - - - - - 



def limpiaDatos() :
    codigoPaisEntry.set("")
    codigoPaisEntry.focus()
    
def listaPrecios():
    global c, text
    hoy=datetime.now()
    dia_hoy = hoy.strftime("%d/%m/%Y")

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

    nombre_archivo="Listadoprecios_"+nombre_pais+".pdf"
    c=canvas.Canvas(nombre_archivo, pagesize=A4)
    cabecera(nombre_pais)

    renglon=0
    text.textLine("Producto                                                    Precio")
    text.textLine("")

    for li in lista:
        renglon=renglon+1
        cod_prod=li[0]
        precio_prod=li[1]
        #print(cod_prod)
        prod.busca_producto(cod_prod)
                
        #print(prod.nombre_producto," precio: ",'{:.2f}'.format(precio_prod))
        n_p=prod.nombre_producto+"                                                "
        n_p=n_p[0:50]
        p_p='{:10.2f}'.format(precio_prod)

        text.textLine(n_p+"      "+p_p)

        if renglon==50:
            renglon=0
            pie(pagina,dia_hoy)
            pagina+=1
            # nueva hoja
            cabecera(nombre_pais)
            text.textLine("Producto                                                    Precio")
            text.textLine("")


    pie(pagina,dia_hoy)
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
    

def pie(pag, dia):
    global c, text
    c.drawText(text)
    text=c.beginText(40,40)
    text.setFont("Times-Roman",8)
    text.textLine("Programado por: Osvaldo G. Campilongo                        página: "+str(pag)+"       Fecha: "+dia)
    c.drawText(text)
    c.showPage()
    



# - - - - - - - - - - Prog. Principal - - - - - - - 


raiz=Tk()
raiz.title("Lista Precios x Pais")
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




# - - - - - Entrys - - - - - - 

lista=[]
lista_pais=Paises.Paises()
lista=lista_pais.leer_lista(lista)
codigoPaisEntry=ttk.Combobox(frame,values=lista,width=40,state="readonly")
codigoPaisEntry.grid(row=0,column=1,sticky="w",padx=5, pady=5)
codigoPaisEntry.config(font="Arial 10")




limpiarBtn=Button(frame,text="Limpiar", command=lambda:limpiaDatos())
limpiarBtn.grid(row=2,column=0,columnspan=2,ipady=5, pady=5)
limpiarBtn.config(width="60")

listarBtn=Button(frame,text="Listar Precios", command=lambda:listaPrecios())
listarBtn.grid(row=3,column=0,columnspan=2,ipady=5, pady=5)
listarBtn.config(width="60")

salirBtn=Button(frame,text="Salir", command=raiz.destroy)
salirBtn.grid(row=4,column=0,columnspan=2,ipady=5, pady=5)
salirBtn.config(width="60")

codigoPaisEntry.focus()
    
raiz.mainloop()

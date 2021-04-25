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
raiz.title("Listado de Productos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")


textoLbl=Label(frame,text="Genera pdf con listado: ")
textoLbl.config(bg=color)
textoLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

listarBtn=Button(frame,text="Listar", command=lambda:listaProductos())
listarBtn.grid(row=4,column=1,sticky="w",ipady=5, pady=5, padx=15)
listarBtn.config(width="10")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=7,column=0,columnspan=2,ipady=5)
salirBtn.config(width="60")
    
raiz.mainloop()

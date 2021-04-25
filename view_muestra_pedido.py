# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from Clases import Pedidos,Clientes, Paises, Productos, Pais_Precios, Items



color="#f2d05e"
# - - - - - - - funciones - - - - - - - - 
def buscaPedido():
    
    ped=Pedidos.Pedidos()
    print(codigoCliEntry.get(), len(codigoCliEntry.get()))
    lista_pedidos=ped.lista_pedidos(codigoCliEntry.get())

    
    #print(lista_pedidos)

    
    fechaPedEntry=ttk.Combobox(frame,values=lista_pedidos,width=12, state="readonly")
    fechaPedEntry.grid(row=4,column=5,sticky="w",padx=5, pady=5)
    fechaPedEntry.config(font="Arial 10")

    okBtn=Button(frame,text="Ok" ,command=lambda:buscar_pedido_elegido())
    okBtn.grid(row=4,column=5,ipady=5,padx=2,sticky="e")
    okBtn.config(width="3")

    


    def buscar_pedido_elegido():
        global fecha,id_cli
        aux=fechaPedEntry.get()
        id_cli=int(aux[0:-13])
        fecha=aux[-10:]
        fechaPedEntry.set(fecha)

        pedidoEntry.delete(1.0,END)
        
        grabarPedBtn['state'] = NORMAL

        ped=Pedidos.Pedidos()
        ped.busca_pedido(id_cli)
        incotermEntry.set(ped.incoterm)
        condicionEntry.set(ped.condicion)
        nota.set(ped.nota)
        seguro.set(ped.seguro_importe)
        flete.set(ped.flete_importe)
        flete_var.set(ped.flete)
        seguro_var.set(ped.seguro)

        # Busca los items dl pedido
        ped_items=Items.Items()
        lista_items=ped_items.busca_item(id_cli)
        total=0.0

        for dato in lista_items:
            p_total=dato[-15:-1]
            p_total=p_total.strip()
            p_total=p_total.replace(",","")
            total=total+float(p_total)
            pedidoEntry.insert(END,dato+"\n")

        total_ped.set(str('{:,.2f}'.format(total)))
        

        #p_total=p_total[-15:-1]
        #item=p.cod_producto+" - "+producto+" - "+cant+ " - "+pre+" - "+p_total

    

def imprimirPed():
    global fecha,cod_cli, id_trib, id_cli
    
    w , h=A4
    nombre_archivo="Proforma"+str('{:06d}'.format(id_cli))+".pdf"
    c=canvas.Canvas(nombre_archivo, pagesize=A4)
    c.rect(30,30,530,770)

    c.drawImage("./images/Logo-Pharmavet-300x127.jpg",50,730,width=150,height=60)
    
    text=c.beginText(210,730)
    text.setFont("Times-Roman",14)
    text.textLine("PEDIDO "+nombre.get())
    c.drawText(text)

    text=c.beginText(50,700)
    text.setFont("Times-Roman",10)
    text.textLine("Fecha: "+fecha+"                      Cod. Cliente: "
    +cod_cli+"     ID Tributaria: "+id_trib+"    Proforma: PF"+str('{:06d}'.format(id_cli)))

    text.textLine("")

    text.setFont("Courier",9)
    text.textLine("Código Prod                 Producto              Cantidad    Precio U$S        Total U$S")
    
    #lineas de separación
    c.line(30,690,560,690)
    text.textLine("")
    c.line(35,670,555,670)


    ped_items=pedidoEntry.get(1.0,END)
    x=0
    while True:
        
        linea=ped_items[x:x+88]
        text.textLine(linea)

        x=x+89
        z=ped_items[x:x+10]
        if not (z.isdigit()):
            break
    
    text.textLine("")
    
    text.textLine("TOTAL FOB - Rosario - Santa Fe - Argentina                                     "+totalEntry.get())
    text.textLine("")
    text.textLine("El importe corresponde a Dólares Estadounidenses")
    text.textLine("País de Origen: Argentina")
    text.textLine("")
    text.textLine("")
    
    
    if flete_var.get():
        text.textLine("Anexos de Costo de Seguro y Flete: ")
        text.textLine("Flete:        "+str(flete.get()))
        text.textLine("Seguro:       "+str(seguro.get()))
        
    c.drawText(text)

    text=c.beginText(40,40)
    text.setFont("Times-Roman",6)
    text.textLine("Programado por: Osvaldo G. Campilongo")
    c.drawText(text)
    c.showPage()
    c.save()
    return

    



def limpiar_cliente():
    codigoCliEntry.set("")
    nombre.set("")
    localidad.set("")
    nom_pais.set("")    
    incotermEntry.set("")
    condicionEntry.set("")
    nota.set("")
    seguro.set("")
    flete.set("")
    nuevoItemBtn['state'] = DISABLED
    grabarPedBtn['state'] = DISABLED
    pedidoEntry.delete(1.0,END)
    flete_var.set(0)
    seguro_var.set(0)
    total_ped.set("")
        
    codigoCliEntry.focus()

def confirma_cliente(cod):
    global cod_pais, id_trib, cod_cli
    f=True
    if len(cod)>6:
        cod=cod[0:6]
        codigoCliEntry.set(cod)


    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
             messagebox.showerror("ERROR", "Código de cliente está errado")
             return
        f=False
    
    if not f :
        messagebox.showerror("ERROR", "Faltó completar algún Campo")
        return

    #messagebox.showinfo("CORRECTO", "Todo bien")
    cli=Clientes.Clientes()
    
    cli.buscar_cliente(cod)
    cod_cli=cod
    id_trib=cli.id_tributaria

    pais=Paises.Paises()
    cod_pais=cli.cod_pais
    nombre_pais=pais.busca_nombre(cli.cod_pais)

    nombre.set(cli.nombre)
    localidad.set(cli.localidad)
    nom_pais.set(nombre_pais)

    nuevoItemBtn['state'] = NORMAL
    
    confirmaBtn.focus()
    

    

# - - - - - - - - - - Prog. Principal - - - - - - - 
raiz=Tk()
raiz.title("Muestra Pedidos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

# - - - - - -  Variables Globales - - - - - - - - 
cod_pais=""
cod_producto=""
fecha=""
id_trib=""
cod_cli=""
id_cli=0
# - - - - - -  Variables para los Entry - - - - - -

nombre = StringVar()
localidad = StringVar()
nom_pais = StringVar()
incoterm = StringVar()
seguro=StringVar()
flete=StringVar()
nota=StringVar()
total_ped=DoubleVar()



# - - - - -  Labels - - - - - -
pedidosLbl=Label(frame,text="Muestra Pedidos")
pedidosLbl.config(bg=color,font="Arial 25")
pedidosLbl.grid(row=0,column=0,padx=5, pady=5, columnspan=5)

codigoCliLbl=Label(frame,text="Código Cliente: ")
codigoCliLbl.config(bg=color)
codigoCliLbl.grid(row=1,column=0,sticky="e",padx=5, pady=5)

nombreLbl=Label(frame,text="Nombre: ")
nombreLbl.config(bg=color)
nombreLbl.grid(row=1,column=3,sticky="e",padx=5, pady=5)

localidadLbl=Label(frame,text="Localidad: ")
localidadLbl.config(bg=color)
localidadLbl.grid(row=2,column=0,sticky="e",padx=5, pady=5)

nomPaisLbl=Label(frame,text="País: ")
nomPaisLbl.config(bg=color)
nomPaisLbl.grid(row=2,column=3,sticky="e",padx=5, pady=5)

incotermLbl=Label(frame,text="INCOTERM: ")
incotermLbl.config(bg=color)
incotermLbl.grid(row=3,column=0,sticky="e",padx=5, pady=5)

condicionLbl=Label(frame,text="Condición\n de Venta: ")
condicionLbl.config(bg=color)
condicionLbl.grid(row=4,column=0,sticky="e",padx=5, pady=5)

pedidoLbl=Label(frame,text="Pedido: ")
pedidoLbl.config(bg=color)
pedidoLbl.grid(row=7,column=0,sticky="e",padx=5, pady=5)

# - - - - - Entrys - - - - - - 
lista=[]
lista_clientes=Clientes.Clientes()
lista=lista_clientes.leer_lista(lista)
codigoCliEntry=ttk.Combobox(frame,values=lista,width=30,state="readonly")
codigoCliEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5,columnspan=2)
codigoCliEntry.config(font="Arial 10")


nombreEntry=Entry(frame,textvariable=nombre,width=30,state="readonly")
nombreEntry.grid(row=1,column=4,sticky="w",padx=5, pady=5, columnspan=2)
nombreEntry.config(font="Arial 15")


localidadEntry=Entry(frame,textvariable=localidad,state="readonly")
localidadEntry.grid(row=2,column=1,sticky="w",padx=5, pady=5,columnspan=2)
localidadEntry.config(font="Arial 15")


nomPaisEntry=Entry(frame,textvariable=nom_pais,width=30,state="readonly")
nomPaisEntry.grid(row=2,column=4,sticky="w",padx=5, pady=5)
nomPaisEntry.config(font="Arial 10")


incoterms=[
    "FOB-Rosario-Santa FE-ARG", 
    "FOB-Buenos Aires-ARG",
    "CIF-Destino"]
incotermEntry=ttk.Combobox(frame,values=incoterms,width=30, state=DISABLED)
incotermEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,columnspan=2)
incotermEntry.config(font="Arial 12")

seguro_var = IntVar()
seguroCheck=ttk.Checkbutton(frame,text="Seguro", state=DISABLED,variable=seguro_var)
seguroCheck.grid(row=3,column=3,sticky="e")

seguroEntry=Entry(frame,textvariable=seguro, state=DISABLED,width=15)
seguroEntry.grid(row=3,column=4,sticky="w",padx=5, pady=5)
seguroEntry.config(font="Arial 10")

fechaPedLbl=Label(frame,text="Fecha Pedido",width=12)
fechaPedLbl.grid(row=3,column=5,sticky="w", pady=5)
fechaPedLbl.config(font="Arial 10", bg=color)

condiciones=[
    "100% Adelantado", 
    "50% Adelantado, 50% a 30 días F.Emb.",
    "A 60 días F. Embarque",
    "A 90 días F. Embarque"]
condicionEntry=ttk.Combobox(frame,values=condiciones,width=30, state=DISABLED)
condicionEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5,columnspan=2)
condicionEntry.config(font="Arial 12")

flete_var = IntVar()
fleteCheck=ttk.Checkbutton(frame,text="Flete", state=DISABLED,variable=flete_var)
fleteCheck.grid(row=4,column=3,sticky="e")

fleteEntry=Entry(frame,textvariable=flete, state=DISABLED,width=15)
fleteEntry.grid(row=4,column=4,sticky="w", pady=5)
fleteEntry.config(font="Arial 10")

#fechas_pedido=[]
#fechaPedEntry=ttk.Combobox(frame,values=fechas_pedido,width=12, state=DISABLED)
#fechaPedEntry.grid(row=4,column=5,sticky="w",padx=5, pady=5)
#fechaPedEntry.config(font="Arial 10", state=DISABLED)

confirmaBtn=Button(frame,text="Confirma Cliente" ,command=lambda:confirma_cliente(codigoCliEntry.get()))
confirmaBtn.grid(row=5,column=1,ipady=5,sticky="w")
confirmaBtn.config(width="15")

limpiaBtn=Button(frame,text="Limpiar Datos", command=lambda:limpiar_cliente())
limpiaBtn.grid(row=5,column=2,ipady=5,sticky="w")
limpiaBtn.config(width="15")

notaLbl=Label(frame,text="Nota: ")
notaLbl.config(bg=color)
notaLbl.grid(row=5,column=3,sticky="e",padx=5)

notaEntry=Entry(frame,textvariable=nota,width=50)
notaEntry.grid(row=5,column=4,sticky="w",padx=5, columnspan=2)
notaEntry.config(font="Arial 10")

pedidoLineaLbl=Label(frame,text="Código Prod                 Producto              Cantidad    Precio U$S        Total U$S")
pedidoLineaLbl.config(bg="#3390ff",font="Courier 10")
pedidoLineaLbl.grid(row=6,column=1,sticky="w",padx=5, pady=5, columnspan=4)

totalEntry=Entry(frame,textvariable=total_ped,width=20)
totalEntry.grid(row=6,column=5,sticky="w",padx=5)
totalEntry.config(font="Arial 10")


pedidoEntry=Text(frame,width=90, height=10)
pedidoEntry.grid(row=7,column=1,sticky="w",padx=5, pady=5, columnspan=4,rowspan=4)
pedidoEntry.config(font="Courier 10")

nuevoItemBtn=Button(frame,text="Busca Pedido", state=DISABLED,command=lambda:buscaPedido())
nuevoItemBtn.grid(row=7,column=5,ipady=5)
nuevoItemBtn.config(width="20")
# FALTA: Desactivar datos de incoterm, condiciones, seguro y flete hasta confirmar cliente
# Activarlos una vez que fijemos el pedido

grabarPedBtn=Button(frame,text="Imprime Proforma", state=DISABLED, command=lambda:imprimirPed())
grabarPedBtn.grid(row=8,column=5,ipady=5)
grabarPedBtn.config(width="20")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=9,column=5,columnspan=2,ipady=5)
salirBtn.config(width="20")

codigoCliEntry.focus()
    
raiz.mainloop()

#dato_p=Pedidos.Pedidos()

#dato_p.guardar_pedidos()
    





    














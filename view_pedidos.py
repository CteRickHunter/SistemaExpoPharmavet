# Programa para carga de datos en BBDD SQLite

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

from Clases import Pedidos,Clientes, Paises, Productos, Pais_Precios, Items



color="#f2d05e"
# - - - - - - - funciones - - - - - - - - 
def buscaItem():
    global hija

    prod=Productos.Productos()
    lista_productos=prod.leer_lista()

    hija=Toplevel()
    hija.title("Carga de Items")
    hija.iconbitmap("images/logo.ico")
    hija.resizable(0,0)

    frame2=Frame(hija)
    frame2.config(bg=color, width="650", height="550")
    frame2.pack(fill="both", expand="False")
        
    listaProdEntry=ttk.Combobox(frame2,values=lista_productos,width=40,state="readonly")
    listaProdEntry.grid(row=1,column=1,sticky="w",padx=5, pady=5)
    listaProdEntry.config(font="Arial 10")

    cantLabel=Label(frame2,text="Cantidad")
    cantLabel.grid(row=0,column=2,ipady=5)
    cantLabel.config(bg=color)

    cantidad=StringVar()
    cantProdEntry=Entry(frame2,textvariable=cantidad,width=10)
    cantProdEntry.grid(row=1,column=2,ipady=5)

    aux1Lbl=Label(frame2,text="")
    aux1Lbl.grid(row=2,column=1,ipady=5)
    aux1Lbl.config(bg=color)

    eligeItemBtn=Button(frame2,text="Elige Item", command=lambda:agregaItem(listaProdEntry.get(),cantProdEntry.get()))
    eligeItemBtn.grid(row=3,column=1,ipady=5)
    eligeItemBtn.config(width="20")

    aux2Lbl=Label(frame2,text="")
    aux2Lbl.grid(row=4,column=1,ipady=5)
    aux2Lbl.config(bg=color)
    

    
    def agregaItem(item,cant):
        global cod_pais
        global cod_producto
        global hija
        
        if item=="":
            messagebox.showerror("ERROR", "Debe elegir un producto")
            hija.destroy()
            return

        if  cant=="" or int(cant)<1:
            messagebox.showerror("ERROR", "Cantidad no puede ser menor a 1")
            hija.destroy()
            return
        # Busca Producto y formatea
        cod=item[0:10]
        p=Productos.Productos()
        p.busca_producto(cod)
        cod_producto=cod
        producto=p.nombre_producto+"                              "
        producto=producto[0:35]

        # Formatea Cantidad
        cant="         "+cant+" "
        cant=cant[-8:-1]

        # busca precio y formatea
        pp=Pais_Precios.Pais_Precios()
        precio=pp.busca_precio(cod_pais, cod_producto)
        pre="          "+str(precio)+" "
        pre=pre[-11:-1]
        #total= float(precio) * float(cant)
        #total_ped.set(total_ped.get()+total)

        #p_total="              "+str('{:,.3f}'.format(total))
        #p_total=p_total[-15:-1]

        # Muestro precio y permito ajustar valor
        aux1Lbl=Label(frame2,text="precio: ")
        aux1Lbl.grid(row=2,column=1,ipady=5,sticky="e")
        aux1Lbl.config(bg=color)

        precio_un=StringVar()
        precioEntry=Entry(frame2,textvariable=precio_un,width=10)
        precioEntry.grid(row=2,column=2,ipady=5)
        precio_un.set(pre)
        

        #item=p.cod_producto+" - "+producto+" - "+cant+ " - "+pre+" - "+p_total

        #confirmaBtn=Button(frame2,text="Confirma precio", command=lambda:confirma_precio(item))
        confirmaBtn=Button(frame2,text="Confirma precio", command=lambda:confirma_precio(cod,producto,cant,precioEntry.get()))
        confirmaBtn.grid(row=4,column=1,ipady=5)
        confirmaBtn.config(width="20")
        # cod,producto,cant,precioEntry.get()
        

        

def confirma_precio(cod,pro,cant,pre):
    global hija
    total= float(pre) * float(cant)
    p_total="              "+str('{:,.3f}'.format(total))
    p_total=p_total[-15:-1]

    total_ped.set(total_ped.get()+total)

    pre="          "+pre+" "
    pre=pre[-11:-1]

    item=cod+" - "+pro+" - "+cant+ " - "+pre+" - "+p_total
    # Activa boton de grabar pedido
    grabarPedBtn['state'] = NORMAL

    pedidoEntry.insert(END,item+"\n")
    hija.destroy()

def grabarPed():
    hoy=datetime.now()
    dia_hoy = hoy.strftime("%d/%m/%Y")

    # verificar seguro y flete
    #Seguro - - - 
    #print(seguro.get(), type(seguro.get()))
    if not seguro_var.get():
        #print("es Falso")
        seguro.set(0)
    else:
        #print("es Verdadero")
        if seguro.get()=="":
            #print("Esta vacio")
            seguro.set(0)
            
        else:
            if seguro.get().isdigit():
                # El dato del seguro es correcto
                #print(float(seguro.get()))
                pass
            else:
                seguro.set(0)
    #Flete - - - 
    #print(flete.get(), type(flete.get()))
    if not flete_var.get():
        #print("es Falso")
        flete.set(0)
    else:
        #print("es Verdadero")
        if flete.get()=="":
            #print("Esta vacio")
            flete.set(0)
            
        else:
            if flete.get().isdigit():
                # El dato del flete es correcto
                #print(float(flete.get()))
                pass
            else:
                flete.set(0)
    #  Fin control Seguro y Flete

     
    # - - - - - - - - - - - 
    nuevo_pedido=Pedidos.Pedidos(dia_hoy,codigoCliEntry.get(),incotermEntry.get(),seguro_var.get(),seguro.get(),flete_var.get(),flete.get(),condicionEntry.get(),nota.get())
    nuevo_pedido.guardar_pedidos()

    nro_pedido=nuevo_pedido.ultimo_registro()

    texto=pedidoEntry.get(1.0,END)
    print(texto)

    linea=Items.Items()
    x=0
    y=88
    # leo las lineas del pedido y grabo
    while True:
        
        linea.id_pedido=nro_pedido
        linea.cod_producto=texto[x:x+10]
        linea.cantidad=int(texto[x+50:x+58])
        linea.precio=float(texto[x+60:x+71])
        # Graba registro Item
        linea.guardar_producto()

        #print(texto[x:y])
        #print("- - - -",texto[x:x+10]," - - - - - ")
        x=x+89
        y=y+89
        z=texto[x:x+10]
        if not (z.isdigit()):
            break
        
    limpiar_cliente()
        
    



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
    global cod_pais
    f=True
    if len(cod)>6:
        cod=cod[0:6]
        codigoCliEntry.set(cod)


    if cod=="" or len(cod)!=6:
        if len(cod)!=6:
             messagebox.showerror("ERROR", "Código de cliente está errado")
             return
        f=False
    
    if incotermEntry.get()=="" :
        messagebox.showerror("ERROR", "INCOTERM: Falta Completar")
        return

    if condicionEntry.get()=="" :
        messagebox.showerror("ERROR", "Condición de venta: Falta Completar")
        return

    if not f :
        messagebox.showerror("ERROR", "Faltó completar algún Campo")
        return

    #messagebox.showinfo("CORRECTO", "Todo bien")
    cli=Clientes.Clientes()
    
    cli.buscar_cliente(cod)
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
raiz.title("Carga de Pedidos")
raiz.iconbitmap("images/logo.ico")
raiz.resizable(0,0)

frame=Frame(raiz)
frame.config(bg=color, width="650", height="350")
frame.pack(fill="both", expand="False")

# - - - - - -  Variables Globales - - - - - - - - 
cod_pais=""
cod_producto=""
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
pedidosLbl=Label(frame,text="Pedidos")
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
incotermEntry=ttk.Combobox(frame,values=incoterms,width=30,state="readonly")
incotermEntry.grid(row=3,column=1,sticky="w",padx=5, pady=5,columnspan=2)
incotermEntry.config(font="Arial 12")

seguro_var = IntVar()
seguroCheck=ttk.Checkbutton(frame,text="Seguro",variable=seguro_var)
seguroCheck.grid(row=3,column=3,sticky="e")

seguroEntry=Entry(frame,textvariable=seguro,width=15)
seguroEntry.grid(row=3,column=4,sticky="w",padx=5, pady=5)
seguroEntry.config(font="Arial 10")

condiciones=[
    "100% Adelantado", 
    "50% Adelantado, 50% a 30 días F.Emb.",
    "A 60 días F. Embarque",
    "A 90 días F. Embarque"]
condicionEntry=ttk.Combobox(frame,values=condiciones,width=30,state="readonly")
condicionEntry.grid(row=4,column=1,sticky="w",padx=5, pady=5,columnspan=2)
condicionEntry.config(font="Arial 12")

flete_var = IntVar()
fleteCheck=ttk.Checkbutton(frame,text="Flete",variable=flete_var)
fleteCheck.grid(row=4,column=3,sticky="e")

fleteEntry=Entry(frame,textvariable=flete,width=15)
fleteEntry.grid(row=4,column=4,sticky="w",padx=5, pady=5)
fleteEntry.config(font="Arial 10")


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

nuevoItemBtn=Button(frame,text="Nuevo Item", state=DISABLED,command=lambda:buscaItem())
nuevoItemBtn.grid(row=7,column=5,ipady=5)
nuevoItemBtn.config(width="20")

grabarPedBtn=Button(frame,text="Grabar Pedido", state=DISABLED, command=lambda:grabarPed())
grabarPedBtn.grid(row=8,column=5,ipady=5)
grabarPedBtn.config(width="20")


salirBtn=Button(frame,text="Salir",command=raiz.destroy)
salirBtn.grid(row=9,column=5,columnspan=2,ipady=5)
salirBtn.config(width="20")

codigoCliEntry.focus()
    
raiz.mainloop()

#dato_p=Pedidos.Pedidos()

#dato_p.guardar_pedidos()
    





    














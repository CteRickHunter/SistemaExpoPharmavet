import sqlite3
from Clases import Productos

class Items:
    
    def __init__(self,id="",id_p="",cod_p="",cant=0,pre=0.0):
        self.id=id
        self.id_pedido=id_p
        self.cod_producto=cod_p
        self.cantidad= cant
        self.precio= pre

    def guardar_producto(self):

        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("INSERT INTO Item_Pedido (id_pedido,cod_producto,cantidad,precio)"+ 
        "VALUES("+str(self.id_pedido)+",'"+self.cod_producto+"',"+str(self.cantidad)+","+str(self.precio)+")")
        
        con.commit()
        con.close()

    def busca_item(self,id):
    
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("SELECT * FROM Item_Pedido WHERE id_pedido="+str(id))
        con.commit()
        datos_lineas=cur.fetchall()
        lista=[]
        for dato in datos_lineas:
            prod=Productos.Productos()
            prod.busca_producto(dato[2])

            producto=prod.nombre_producto+"                              "
            producto=producto[0:35]

            item=dato[2]+" - "+producto+" - "

            # Formatea Cantidad
            cant="         "+str(dato[3])+" "
            cant=cant[-8:-1]
            item=item+cant+" - "

            # busca precio y formatea
           
            precio=dato[4]
            pre="          "+str(precio)+" "
            pre=pre[-11:-1]
            total= float(precio) * float(cant)
            p_total="              "+str('{:,.3f}'.format(total))
            p_total=p_total[-15:-1]
            
            item=item+pre+" - "+p_total
            lista.append(item)


            #item=p.cod_producto+" - "+producto+" - "+cant+ " - "+pre+" - "+p_total
               
        con.close()
        return lista


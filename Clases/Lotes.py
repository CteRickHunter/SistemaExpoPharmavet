import sqlite3


class Lotes:
    
    def __init__(self,nro="",f_elab="",f_venc="",cod=""):
        self.nro_lote=nro
        self.fecha_elab=f_elab
        self.fecha_venc=f_venc
        self.cod_prod_base=cod

    def guardar_lote(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        

        cur.execute("INSERT INTO Lotes VALUES('"+self.nro_lote+"','"+
        self.fecha_elab+"','"+self.fecha_venc+"','"+self.cod_prod_base+"')")
        con.commit()
        con.close()

    def cambiar_lote(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("UPDATE Lotes set fecha_elaboracion='"+self.fecha_elab+
        "', fecha_vencimiento='"+self.fecha_venc+
        "', cod_producto_base='"+self.cod_prod_base+
        "' WHERE nro_lote='"+self.nro_lote+"'")

        con.commit()
        con.close()

    

    def setear_lote(self,nro,f_elab,f_venc,cod):
        self.nro_lote=nro
        self.fecha_elab=f_elab
        self.fecha_venc=f_venc
        self.cod_prod_base=cod
    

    def leer_lista(self,cod):
        lista=[]
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT nro_lote, fecha_vencimiento FROM Lotes WHERE cod_producto_base='"+cod+"' ORDER BY nro_lote DESC")
        con.commit()
        datos_lotes=cur.fetchall()
        for dato in datos_lotes:
            lote=dato[0]+"        "
            lote=lote[0:8]
            dato_txt=lote+"-*- Venc:"+dato[1]
            lista.append(dato_txt)

        con.close()
        return lista

    def busca_lote(self,cod):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT nro_lote,fecha_elaboracion, fecha_vencimiento, cod_producto_base FROM Lotes WHERE nro_lote='"+cod+"'")
        con.commit()
        dato_lote=cur.fetchone()
        self.nro_lote=dato_lote[0]
        self.fecha_elab=dato_lote[1]
        self.fecha_venc=dato_lote[2]
        self.cod_prod_base=dato_lote[3]

        con.close()
        
    def existe_lote(self,lote):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT fecha_elaboracion FROM Lotes WHERE nro_lote='"+lote+"'")
        con.commit()
        dato=cur.fetchone()
        
        if dato:
            con.close()
            return True
            
        else:
            con.close()
            return False
            

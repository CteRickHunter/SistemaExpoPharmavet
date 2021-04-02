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

    def setear_lote(self,nro,f_elab,f_venc,cod):
        self.nro_lote=nro
        self.fecha_elab=f_elab
        self.fecha_venc=f_venc
        self.cod_prod_base=cod
    


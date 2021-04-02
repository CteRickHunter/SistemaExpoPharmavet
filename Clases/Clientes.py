import sqlite3


class Clientes:
    
    def __init__(self,cod="",nom="",dir="",loc="",pais="",cod_trib="",cond="",tel="",mail=""):
        self.cod_cliente=cod
        self.nombre=nom
        self.direccion=dir
        self.localidad=loc
        self.cod_pais=pais
        self.id_tributaria=cod_trib
        self.condicion_venta=cond
        self.telefono=tel
        self.correo_electronico=mail

    def guardar_clientes(self):

        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
    
        cur.execute("INSERT INTO Clientes VALUES('"+self.cod_cliente+
        "','"+self.nombre+"','"+self.direccion+
        "','"+self.localidad+"','"+self.cod_pais+
        "','"+self.id_tributaria+"','"+self.condicion_venta+
        "','"+self.telefono+"','"+self.correo_electronico+"')")
        
        con.commit()
        con.close()

    def setear_clientes(self,cod,nom,dir,loc,pais,cod_trib,cond,tel,mail):
        self.cod_cliente=cod
        self.nombre=nom
        self.direccion=dir
        self.localidad=loc
        self.cod_pais=pais
        self.id_tributaria=cod_trib
        self.condicion_venta=cond
        self.telefono=tel
        self.correo_electronico=mail
    


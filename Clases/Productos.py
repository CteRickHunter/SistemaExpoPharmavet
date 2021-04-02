import sqlite3


class Productos:
    
    def __init__(self,cod1="",cod2="",nom="",peso=1.0,vol=1.0):
        self.cod_producto=cod1
        self.cod_producto_base=cod2
        self.nombre_producto=nom
        self.peso_producto= peso
        self.volumen_producto= vol

    def guardar_producto(self):

        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
    
        cur.execute("INSERT INTO Productos VALUES('"+self.cod_producto+
        "','"+self.cod_producto_base+"','"+self.nombre_producto+"',"+
        self.peso_producto+","+self.volumen_producto+")")
        
        con.commit()
        con.close()

    def setear_producto(self,cod1,cod2,nom,peso=1.0,vol=1.0):
        self.cod_producto = cod1
        self.cod_producto_base = cod2
        self.nombre_producto = nom
        self.peso_producto = peso
        self.volumen_producto = vol
    


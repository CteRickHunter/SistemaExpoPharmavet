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

    def leer_lista(self):
        lista=[]
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_producto,nombre_producto_comercial FROM Productos ORDER BY nombre_producto_comercial")
        con.commit()
        datos_productos=cur.fetchall()
        con.close()
        for dato in datos_productos:
            dato_txt=str(dato[0])+"-*-"+str(dato[1])
            lista.append(dato_txt)

        return lista
        

    def busca_producto(self,cod_prod):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT * FROM Productos WHERE cod_producto='"+cod_prod+"'")
        con.commit()
        dato=cur.fetchone()
        self.cod_producto = dato[0]
        self.cod_producto_base = dato[1]
        self.nombre_producto = dato[2]
        self.peso_producto = dato[3]
        self.volumen_producto = dato[4]
        con.close()
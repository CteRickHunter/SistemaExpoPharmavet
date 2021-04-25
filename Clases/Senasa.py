import sqlite3
from tkinter import messagebox

class Senasa:
    
    def __init__(self , cod="",nom="",nroexp="",nrocer="",nmn=""):
        self.cod_producto_base=cod
        self.nombre_producto_SENASA=nom
        self.nro_expediente=nroexp
        self.nro_certificado=nrocer
        self.nomenclador=nmn

    def guardar_senasa(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("INSERT INTO Datos_SENASA VALUES('"+self.cod_producto_base+"','"+
        self.nombre_producto_SENASA+"','"+self.nro_expediente+"','"+self.nro_certificado+
        "','"+self.nomenclador+"')")
        
        con.commit()
        con.close()

    def actualizar_producto(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
    
        cur.execute("UPDATE Datos_SENASA SET "+
        "nombre_producto_SENASA='"+self.nombre_producto_SENASA+"',"+
        "nro_expediente='"+self.nro_expediente+"',"+
        "nro_certificado='"+self.nro_certificado+"',"+
        "nomenclador='"+self.nomenclador+"'"+
        " WHERE cod_producto_base='"+self.cod_producto_base+"'")
        
        con.commit()
        con.close()

    def setear_senasa(self,cod,nom,nroexp,nrocer,nmn):
        self.cod_producto_base=cod
        self.nombre_producto_SENASA=nom
        self.nro_expediente=nroexp
        self.nro_certificado=nrocer
        self.nomenclador=nmn

    def buscar(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        if self.cod_producto_base!="":
            try:
                cur.execute("SELECT Datos_SENASA WHERE cod_producto_base="+self.cod_producto_base)
            except:
                messagebox.showerror("ERROR", "No fue encontrada ninguna coincidencia")
                con.close()
                return

        else:
            messagebox.showerror("ERROR", "No puede estar vacía la búsqueda")
            con.close()
            return

        con.commit()
        con.close()

    
    def leer_lista(self,lista):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_producto_base, nombre_producto_SENASA FROM Datos_SENASA ORDER BY nombre_producto_SENASA")
        con.commit()
        datos_Senasa=cur.fetchall()
        for dato in datos_Senasa:
            dato_txt=dato[0]+"-*-"+dato[1]
            lista.append(dato_txt)

        con.close()
        return lista

    def busca_nombre(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("SELECT * FROM Datos_SENASA WHERE cod_producto_base='"+self.cod_producto_base+"'")
        con.commit()
        dato=cur.fetchone()

        self.nombre_producto_SENASA=dato[1]
        self.nro_expediente=dato[2]
        self.nro_certificado=dato[3]
        self.nomenclador=dato[4]
        
        con.close()

    def existe_producto(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT * FROM Datos_SENASA WHERE cod_producto_base='"+self.cod_producto_base+"'")
        con.commit()
        dato=cur.fetchone()
        
        if dato:
            con.close()
            return True
            
        else:
            con.close()
            return False

    


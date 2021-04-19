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
                return

        else:
            messagebox.showerror("ERROR", "No puede estar vacía la búsqueda")
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
            dato_txt=str(dato[0])+"-*-"+str(dato[1])
            lista.append(dato_txt)

        return lista

        con.close()

    


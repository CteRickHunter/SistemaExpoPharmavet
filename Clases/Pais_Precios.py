import sqlite3
from tkinter import messagebox

class Pais_Precios:
    
    def __init__(self , cod="",prod="",precio=0.0):
        self.cod_pais=cod
        self.cod_producto=prod
        self.precio=precio
        

    def guardar_precio(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("INSERT INTO Pais_Precio VALUES('"+self.cod_pais+"','"+
        self.cod_producto+"',"+self.precio+")")
        
        con.commit()
        con.close()

    def cambia_precio(self,cod,prod,precio):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("UPDATE Pais_Precio set precio="+precio+" WHERE cod_pais='"+cod+"' and cod_producto= '"+prod+"'")
        
        con.commit()
        con.close()

    def setear_precio(self , cod,prod,precio):
        self.cod_pais=cod
        self.cod_producto=prod
        self.precio=precio

    
    

    def busca_precio(self,pais,producto):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT precio FROM Pais_Precio WHERE cod_pais='"+pais+"' AND cod_producto='"+producto+"'")
        con.commit()
        dato=cur.fetchone()
        if not dato:
            messagebox.showerror("ERROR", "No existe precio para ese artículo para ese cliente")
            con.close()
            return
        con.close()
        return dato[0]

        

    def existe_precio(self,pais,producto):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT precio FROM Pais_Precio WHERE cod_pais='"+pais+"' AND cod_producto='"+producto+"'")
        con.commit()
        dato=cur.fetchone()
        
        if dato:
            con.close()
            return True
            
        else:
            con.close()
            return False
            

    def lista_precios(self,pais):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_producto,precio FROM Pais_Precio WHERE cod_pais='"+pais+"' ORDER BY cod_producto")
        con.commit()
        lista=cur.fetchall()
        con.close()
        return lista

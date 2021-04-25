import sqlite3


class Paises:
    
    def __init__(self , cod="",pais="",cuit=""):
        self.cod_pais=cod
        self.pais=pais
        self.cuit_pais=cuit
        

    def guardar_pais(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("INSERT INTO Paises VALUES('"+self.cod_pais+"','"+
        self.pais+"','"+self.cuit_pais+"')")
        
        con.commit()
        con.close()

    def setear_pais(self , cod,pais,cuit):
        self.cod_pais=cod
        self.pais=pais
        self.cuit_pais=cuit

    
    def leer_lista(self,lista):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_pais, pais FROM Paises")
        con.commit()
        datos_paises=cur.fetchall()
        for dato in datos_paises:
            dato_txt=str(dato[0])+"-*-"+str(dato[1])
            lista.append(dato_txt)
        con.close()
        return lista

    def buscar_pais(self,codigo_pais):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_pais, pais FROM Paises WHERE cod_pais='"+codigo_pais+"'")
        con.commit()
        dato_pais=cur.fetchone()
        salida=dato_pais[0]+"-*-"+dato_pais[1]
        
        con.close()
        return salida
        

    def busca_nombre(self,codigo):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT pais FROM Paises WHERE cod_pais='"+codigo+"'")
        con.commit()
        dato=cur.fetchone()
        con.close()
        return dato[0]

        


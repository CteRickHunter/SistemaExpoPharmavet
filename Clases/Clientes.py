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

    def actualiza_cliente(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
    
        cur.execute("UPDATE Clientes SET "+
        "nombre='"+self.nombre+"',"+
        "direccion='"+self.direccion+"',"+
        "localidad='"+self.localidad+"',"+
        "cod_pais='"+self.cod_pais+"',"+
        "id_tributaria='"+self.id_tributaria+"',"+
        "condicion_venta='"+self.condicion_venta+"',"+
        "telefono='"+self.telefono+"',"+
        "correo_electronico='"+self.correo_electronico+"'"+
        " WHERE cod_cliente='"+self.cod_cliente+"'")
        
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
    
    def leer_lista(self,lista):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT cod_cliente,nombre FROM Clientes")
        con.commit()
        datos_clientes=cur.fetchall()
        for dato in datos_clientes:
            dato_txt=str(dato[0])+"-*-"+str(dato[1])
            lista.append(dato_txt)

        return lista

        con.close()
    
    def buscar_cliente(self,codigo):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT * FROM Clientes where cod_cliente='"+codigo+"'")
        con.commit()
        dato=cur.fetchone()
        #print("El dato es: ",dato)
        self.cod_cliente=dato[0]
        self.nombre=dato[1]
        self.direccion=dato[2]
        self.localidad=dato[3]
        self.cod_pais=dato[4]
        self.id_tributaria=dato[5]
        self.condicion_venta=dato[6]
        self.telefono=dato[7]
        self.correo_electronico=dato[8]

        con.close()

    def existe_cliente(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT * FROM Clientes WHERE cod_cliente='"+self.cod_cliente+"'")
        con.commit()
        dato=cur.fetchone()
        
        if dato:
            con.close()
            return True
            
        else:
            con.close()
            return False

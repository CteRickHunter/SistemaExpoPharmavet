import sqlite3


class Pedidos:
    
    def __init__(self,f_ped="",c_cli="",inco="",seguro=0,s_imp=0.0,flete=0,f_imp=0.0,cond="",nota=""):
        self.fecha_pedido=f_ped
        self.cod_cliente=c_cli
        self.incoterm=inco
        self.seguro=seguro
        self.seguro_importe=s_imp
        self.flete=flete
        self.flete_importe=f_imp
        self.condicion=cond
        self.nota=nota

    def guardar_pedidos(self):

        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("INSERT INTO Pedidos (fecha_pedido,cod_cliente,"+
        "incoterm,seguro, seguro_importe,flete,flete_importe,condicion,nota)"+
        " VALUES('"+self.fecha_pedido+"','"+self.cod_cliente+"','"+self.incoterm+"',"+
        str(self.seguro)+","+str(self.seguro_importe)+","+
        str(self.flete)+","+str(self.flete_importe)+",'"+
        self.condicion+"','"+self.nota+"')")
        
        con.commit()
        con.close()
        
    def ultimo_registro(self):
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT id_pedido FROM Pedidos ORDER BY id_pedido DESC LIMIT 1;")
        con.commit()
        dato=cur.fetchone()
        con.close()
        return dato[0]
        

    
    def lista_pedidos(self,cod):
        lista=[]
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        cur.execute("SELECT id_pedido, fecha_pedido FROM Pedidos WHERE cod_cliente='"+cod+"'")
        con.commit()
        datos_pedidos=cur.fetchall()
        con.close()
        for dato in datos_pedidos:
            dato_txt=str(dato[0])+"-*-"+dato[1]
            lista.append(dato_txt)
            
        #print(lista)
        return lista
        
    def busca_pedido(self,id):
        
        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
        
        cur.execute("SELECT * FROM Pedidos WHERE id_pedido="+str(id))
        
        con.commit()
        datos_pedidos=cur.fetchone()
        self.fecha_pedido=datos_pedidos[1]
        self.cod_cliente=datos_pedidos[2]
        self.incoterm=datos_pedidos[3]
        self.seguro=datos_pedidos[4]
        self.seguro_importe=datos_pedidos[5]
        self.flete=datos_pedidos[6]
        self.flete_importe=datos_pedidos[7]
        self.condicion=datos_pedidos[8]
        self.nota=datos_pedidos[9]
        con.close()
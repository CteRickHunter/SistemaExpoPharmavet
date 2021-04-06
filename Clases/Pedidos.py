import sqlite3


class Pedidos:
    
    def __init__(self,f_ped="",c_cli="",inco="",s_txt="",s_imp=0.0,f_txt="",f_imp=0.0,nota=""):
        self.fecha_pedido=f_ped
        self.cod_cliente=c_cli
        self.incoterm=inco
        self.seguro_texto=s_txt
        self.seguro_importe=s_imp
        self.flete_texto=f_txt
        self.flete_importe=f_imp
        self.nota=nota

    def guardar_pedidos(self):

        con=sqlite3.connect("SistemaExpo")
        cur=con.cursor()
    
        cur.execute("INSERT INTO Pedidos VALUES('"+self.fecha_pedido+
        "','"+self.cod_cliente+"','"+self.incoterm+"','"+
        self.seguro_texto+"',"+self.seguro_importe+",'"+
        self.flete_texto+"',"+self.flete_importe+",'"+
        self.nota+"')")
        
        con.commit()
        con.close()

    

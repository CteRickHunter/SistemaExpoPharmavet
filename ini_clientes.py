# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Clientes(
cod_cliente	VARCHAR(6) PRIMARY KEY,
nombre	VARCHAR(50) NOT NULL,
direccion	VARCHAR(50) NOT NULL,
localidad	VARCHAR(50) NOT NULL,
cod_pais	VARCHAR(2) NOT NULL,
id_tributaria	VARCHAR(50) NOT NULL,
condicion_venta	VARCHAR(50),
telefono	VARCHAR(30),
correo_electronico	VARCHAR(60) NOT NULL)''')

conectado.commit()
conectado.close()




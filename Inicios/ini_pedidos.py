# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Pedidos(
id_pedido	 integer primary key autoincrement,
fecha_pedido VARCHAR(10) NOT NULL,
cod_cliente	VARCHAR(6) NOT NULL,
incoterm    VARCHAR(30),
seguro	integer,
seguro_importe	REAL,
flete integer,
flete_importe	REAL,
condicion VARCHAR(30),
nota	TEXT)''')

conectado.commit()
conectado.close()




# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Pedidos(
id_pedido	INTEGER AUTO_INCREMENT PRIMARY KEY,
fecha_pedido VARCHAR(10) NOT NULL,
cod_cliente	VARCHAR(6) NOT NULL,
incoterm    VARCHAR(30) NOT NULL,
seguro_texto	VARCHAR(30) NOT NULL,
seguro_importe	REAL NOT NULL,
flete_texto	VARCHAR(30),
flete_importe	REAL,
nota	TEXT NOT NULL)''')

conectado.commit()
conectado.close()




# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Item(
id	 integer primary key autoincrement,
id_pedido integer NOT NULL,
cod_producto	VARCHAR(10) NOT NULL,
cantidad	integer NOT NULL,
precio	REAL NOT NULL)''')

conectado.commit()
conectado.close()




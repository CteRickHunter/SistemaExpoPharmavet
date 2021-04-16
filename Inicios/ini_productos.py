# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Productos(
cod_producto	VARCHAR(10) PRIMARY KEY,
cod_producto_base	VARCHAR(6) NOT NULL,
nombre_producto_comercial	VARCHAR(50) NOT NULL,
peso_unitario	REAL NOT NULL,
voluman_unitario	REAL NOT NULL)''')

conectado.commit()
conectado.close()




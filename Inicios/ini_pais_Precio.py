# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Pais_Precio(
cod_pais	VARCHAR(2),
cod_producto	VARCHAR(10),
precio	REAL NOT NULL,
PRIMARY KEY (cod_pais, cod_producto))''')

conectado.commit()
conectado.close()




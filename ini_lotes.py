# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Lotes(
nro_lote	VARCHAR(8) PRIMARY KEY,
fecha_elaboracion	VARCHAR(10) NOT NULL,
fecha_vencimiento	VARCHAR(10) NOT NULL,
cod_producto_base	VARCHAR(6) NOT NULL)''')

conectado.commit()
conectado.close()




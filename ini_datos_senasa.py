# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Datos_SENASA(
cod_producto_base	VARCHAR(6) PRIMARY KEY,
nombre_producto_SENASA	VARCHAR(50) NOT NULL,
nro_expediente	VARCHAR(15) NOT NULL,
nro_certificado	VARCHAR(10) NOT NULL,
nomenclador	VARCHAR(15) NOT NULL)''')

conectado.commit()
conectado.close()




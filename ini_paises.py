# Programa para carga de datos en BBDD SQLite

import sqlite3

# - - - - - - - - - - Prog. Principal - - - - - - - 

conectado=sqlite3.connect("SistemaExpo")
puntero=conectado.cursor()
puntero.execute(''' 
CREATE TABLE Paises(
cod_pais	VARCHAR(2) PRIMARY KEY,
pais	VARCHAR(25) NOT NULL,
cuit_pais	VARCHAR(11) NOT NULL)''')

conectado.commit()
conectado.close()




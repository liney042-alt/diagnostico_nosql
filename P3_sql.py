import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.executescript("""
CREATE TABLE clientes(id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE ordenes(id INTEGER PRIMARY KEY, cliente_id INTEGER, estado TEXT);

INSERT INTO clientes VALUES(1, 'Cliente A'), (2, 'Cliente B');
INSERT INTO ordenes VALUES(101, 1, 'recibida'), (102, 2, 'cerrada'), (103, 1, 'recibida');
""")

consulta = """
SELECT ordenes.id, clientes.alias
FROM ordenes
INNER JOIN clientes ON ordenes.cliente_id = clientes.id
WHERE ordenes.estado = 'recibida'
ORDER BY ordenes.id ASC;
"""

print("Resultado de la consulta SQL:")
print(conexion.execute(consulta).fetchall())

conexion.close()
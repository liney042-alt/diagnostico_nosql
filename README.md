# TecnoServicios — Guía Semana 1 (NoSQL)

Este repositorio contiene los artefactos, ejercicios de diagnóstico y pruebas de entorno de la Semana 1.

### Estructura
* `P1_json.py`, `P2_json.py`, `P3_sql.py`: Scripts del diagnóstico individual (A1).
* `docs/`: Documentación del caso (Matriz de modelos A2 y Consultas/Reglas A3).
* `scripts/`: Script JS de prueba y verificación en MongoDB (A4).
* `evidencias/`: Registro del entorno de ejecución.

###  Ejecución de scripts
Para ejecutar los ejercicios del diagnóstico en Python:
python P1_json.py
python P2_json.py
python P3_sql.py


Actividad A1: Diagnóstico de Aprendizajes Previos

Este documento contiene la resolución correspondiente a la Parte A: Diagnóstico Teórico del cuestionario de evaluación inicial sobre bases de datos, estructuras de datos, manejo de archivos y buenas prácticas de desarrollo.

Parte A: Diagnóstico Teórico

1. ¿Qué representan una tabla, una fila y una clave primaria?
Tabla: Representa un conjunto homogéneo de entidades u objetos del negocio.
Ejemplo: La tabla equipos.
Fila (o registro): Representa una instancia única e individual dentro de esa entidad.
Ejemplo: Un portátil marca Lenovo con número de serie XYZ123.
Clave primaria (Primary Key - PK): Es un atributo o campo único e inalterable que identifica inequívocamente a cada fila dentro de la tabla.
Ejemplo: codigo_equipo = 'EQ-1001'.

2. ¿Para qué sirve una clave foránea? ¿Qué problema genera una orden que referencia a un cliente inexistente?
Clave foránea (Foreign Key - FK): Sirve para establecer e imponer una relación de integridad referencial entre dos tablas, vinculando un campo de una tabla secundaria con la clave primaria de una tabla principal.
Problema generado: Genera un registro huérfano. En el contexto del taller, esto impediría notificar avances, facturar el servicio, aplicar garantías o determinar legalmente a quién pertenece el dispositivo entregado.

3. Explica qué devuelve SELECT codigo FROM equipos WHERE tipo = 'portatil';. ¿Modifica registros?
Devuelve: El listado de los códigos de identificación de todos los registros en la tabla equipos cuyo campo tipo sea exactamente 'portatil'.
¿Modifica registros?: No, es una sentencia DQL (Data Query Language) de solo lectura. No altera ni modifica ningún dato guardado en la base de datos.

4. Diferencia una lista y un diccionario en Python. ¿Qué estructura utilizarías para un equipo y para varios equipos?
Diccionario (dict): Estructura clave-valor ideal para representar las propiedades de un único equipo.
equipo = {"codigo": "EQ-01", "tipo": "portatil", "ram_gb": 16}
Lista (list): Secuencia ordenada de elementos ideal para agrupar varios equipos.
equipos = [equipo1, equipo2, equipo3]

5. ¿Son equivalentes false y "false" en JSON? Explica el tipo de cada valor.
No son equivalentes.
false: Es un valor literal de tipo booleano (lógica binaria 0/1 o verdadero/falso).
"false": Es un valor de tipo cadena de texto (string) compuesto por 5 caracteres. En evaluaciones de flujo de varios lenguajes de programación, una cadena no vacía como "false" evalúa como verdadera.

6. Diferencia entre campo ausente, campo con null y campo con cadena vacía ("").
Campo ausente: La clave no existe en el documento o registro.
Campo con null: La clave existe explícitamente pero no tiene un valor asignado o este es desconocido momentáneamente.
Campo con "": La clave tiene un valor asignado de tipo texto, pero no posee caracteres (longitud cero).
Ejemplo (Fecha de cierre de una orden):
Ausente: El campo fecha_cierre no fue incluido en la estructura de la orden.
null: "fecha_cierre": null indica que la orden sigue abierta/activa.
"": "fecha_cierre": "" representa un error común al intentar representar la ausencia de fecha usando texto.

7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?
Retornar datos: Otorga modularidad, reutilización de código y automatización de pruebas, permitiendo entregar el resultado a otras variables o funciones para continuar el procesamiento programático.
Imprimir: Únicamente envía texto a la consola o salida del sistema para visualización del usuario humano, lo que impide que el dato pueda ser procesado por otras partes del sistema.

8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?
Sintaxis del JSON: Verificar la validez del contenido (comas sobrantes, comillas simples en lugar de dobles, etc.).
Ruta y Permisos: Confirmar que la ruta (path) del archivo sea correcta y que existan permisos de lectura en el sistema operativo.
Codificación: Asegurar que el archivo esté guardado con codificación UTF-8.

9. Análisis de formato de fecha: 2026-10-06T13:00:00Z
Información que representa: Formato ISO 8601 en Tiempo Universal Coordinado (UTC, indicado por la Z). Corresponde al año 2026, mes 10 (octubre), día 06, a las 13:00:00 UTC.
Ambigüedades que evita: Elimina la confusión entre día y mes (por ejemplo, 06/10 puede interpretarse como 6 de octubre o 10 de junio), y elimina la incertidumbre de la zona horaria y el siglo.

10. Seguridad en Git: Publicación accidental de credenciales
Acciones inmediatas:
Revocar o rotar de inmediato la contraseña o clave expuesta en el servidor/servicio afectado.
Eliminar el secreto de todo el historial de commits utilizando herramientas como git filter-repo o BFG Repo-Cleaner.
Realizar un force push (git push --force) de los cambios limpios.
¿Es suficiente borrarla del archivo en un nuevo commit?: No. Aunque se elimine en el commit más reciente, la credencial continuará siendo accesible públicamente en el historial previo de commits de Git.

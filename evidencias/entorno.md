# Registro del Entorno de Trabajo (Actividad A4)

### Información del Sistema y Herramienta
* **Entorno de desarrollo:** Visual Studio Code
* **Cliente / Extensión:** MongoDB for VS Code Extension
* **Host / Puerto:** `127.0.0.1:27017`
* **Base de datos:** `tecnoservicios_lab`
* **Colección:** `ordenes_demo`

### Resultado de la Verificación de Entorno
1. Se estableció la conexión local exitosamente desde la extensión de MongoDB para VS Code.
2. Se insertó y validó la existencia del documento `OS-DEMO-001` en la colección `ordenes_demo`.
3. Se verificaron los tipos de datos BSON requeridos para el laboratorio:
    
  +  **Subdocumento:** `equipo` (Object)
  + **Booleano:** `requiere_diagnostico: true`
  + **Fecha:** `fecha_ingreso: ISODate('2026-10-06T13:00:00.000Z')`

### Observación
La verificación del entorno y de la persistencia de datos se completó utilizando la extensión nativa de MongoDB en VS Code, garantizando la correcta integración del entorno local.

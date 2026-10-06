# Matriz de Selección de Modelos NoSQL (Actividad A2)

| Caso | Modelo propuesto | Razón vinculada a una consulta | Límite o costo | Alternativa |
| :--- | :--- | :--- | :--- | :--- |
| **Catálogo de dispositivos** | Documental | Los dispositivos (portátiles, teléfonos, etc.) poseen atributos y especificaciones técnicas heterogéneas. | Inconsistencia de esquemas si no se aplican reglas de validación. | Relacional (SQL) |
| **Sesiones temporales** | Clave-valor | Lectura e inserción rápida por ID de sesión con expiración de datos (TTL). | Sin capacidad para realizar consultas complejas sobre la estructura interna. | Documental |
| **Recorridos de relaciones** | Grafos | Permite navegar eficientemente relaciones complejas N:M entre técnicos, habilidades y servicios. | Menor rendimiento en procesamiento analítico masivo y agregaciones. | Relacional (SQL) |
| **Lecturas por dispositivo/periodo** | Familias de columnas | Escritura masiva y lecturas eficientes filtradas por clave de partición temporal a gran escala. | Flexibilidad limitada para consultas no planificadas en el diseño inicial. | Relacional con particionamiento |

## Situación para conservar SQL
Se mantendría una base de datos relacional (SQL) para el módulo de **Facturación y Contabilidad**, debido a la necesidad de garantizar transacciones ACID estrictas e integridad referencial en los montos y pagos.
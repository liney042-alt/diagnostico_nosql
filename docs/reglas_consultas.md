# Reglas de Negocio y Consultas del Caso TecnoServicios (Actividad A3)

## Matriz de Consultas Previstas (Q01–Q06)

| ID | Necesidad | Actor | Filtros | Campos de Salida | Orden | Frecuencia Estimada |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Q01** | Órdenes pendientes por prioridad y estado | Técnico | estado IN ('recibida', 'en_diagnostico', 'en_reparacion', 'lista_entrega'), prioridad | codigo_orden, equipo.codigo, prioridad, estado, fecha_ingreso | prioridad DESC, fecha_ingreso ASC | Alta (Diaria) |
| **Q02** | Detalle de un equipo y sus características | Técnico | equipo.codigo | equipo.codigo, equipo.tipo, equipo.especificaciones | N/A | Media |
| **Q03** | Órdenes de un cliente por periodo y estado | Recepción / Cliente | cliente_id, fecha_ingreso (rango), estado | codigo_orden, equipo.codigo, estado, fecha_ingreso | fecha_ingreso DESC | Media |
| **Q04** | Órdenes con compromiso vencido a corte | Supervisor | fecha_compromiso < fecha_corte, estado activo | codigo_orden, cliente_alias, fecha_compromiso, dias_retraso | fecha_compromiso ASC | Diaria |
| **Q05** | Historial de órdenes de un equipo | Técnico | equipo.codigo | codigo_orden, fecha_ingreso, fecha_cierre, diagnostico | fecha_ingreso DESC | Media |
| **Q06** | Cantidad de órdenes por tipo de equipo y mes | Administrador | fecha_ingreso (año actual) | equipo.tipo, mes, total_ordenes | mes ASC, total_ordenes DESC | Baja (Mensual) |

## Reglas del Negocio
1. `codigo_equipo` y `codigo_orden` son únicos e inmutables.
2. Cada orden pertenece a un equipo y a un cliente solicitante registrado.
3. Estados válidos: `recibida`, `en_diagnostico`, `en_reparacion`, `lista_entrega`, `cerrada`, `cancelada`.
4. Máximo **una orden activa** por equipo al mismo tiempo.
5. La `fecha_compromiso` debe ser igual o posterior a la `fecha_ingreso`.

## Preguntas para el Cliente
1. ¿Cuál es el procedimiento cuando un cliente decide retirar el equipo sin reparar?
2. ¿Qué plazo máximo de garantía aplica para reabrir una orden cerrada?

## Riesgo Identificado
Permitir el ingreso simultáneo de dos órdenes para el mismo equipo sin haber cerrado la anterior.
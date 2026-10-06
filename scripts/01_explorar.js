// Seleccionar la base de datos de trabajo
db = db.getSiblingDB("tecnoservicios_lab");

// Insertar documento de demostración si no existe
if (db.ordenes_demo.countDocuments({_id: "OS-DEMO-001"}) === 0) {
  db.ordenes_demo.insertOne({
    _id: "OS-DEMO-001",
    cliente_alias: "Cliente ficticio 01",
    equipo: {
      codigo: "EQ-DEMO-001",
      tipo: "portatil",
      accesorios_recibidos: ["cargador", "estuche"]
    },
    falla_reportada: "No enciende",
    prioridad: "alta",
    estado: "recibida",
    requiere_diagnostico: true,
    fecha_ingreso: new Date("2026-10-06T13:00:00Z")
  });
}

// Consultar e imprimir documento
print("\n--- Documento recuperado ---");
printjson(db.ordenes_demo.findOne({_id: "OS-DEMO-001"}));

// Verificación de conteo
print("\n--- Conteo por ID ---");
print("Conteo:", db.ordenes_demo.countDocuments({_id: "OS-DEMO-001"}));

// Verificación de tipos BSON
const orden = db.ordenes_demo.findOne({_id: "OS-DEMO-001"});
print("\n--- Validación de tipos ---");
print("fecha_ingreso es Date:", orden.fecha_ingreso instanceof Date);
print("requiere_diagnostico es Boolean:", typeof orden.requiere_diagnostico === "boolean");
print("accesorios_recibidos es Array:", Array.isArray(orden.equipo.accesorios_recibidos));
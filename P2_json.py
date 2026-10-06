ordenes = [
    {"codigo": "OS-001", "prioridad": "alta", "pendiente": True},
    {"codigo": "OS-002", "prioridad": "normal", "pendiente": True},
    {"codigo": "OS-003", "prioridad": "alta", "pendiente": False},
    {"codigo": "OS-004", "prioridad": "alta"}
]

def seleccionar_pendientes(registros, prioridad):
    resultado = []
    for reg in registros:
        if reg.get("prioridad") == prioridad and reg.get("pendiente") is True:
            resultado.append(reg["codigo"])
    return resultado

print("Prueba 1 (Prioridad alta):", seleccionar_pendientes(ordenes, "alta"))
print("Prueba 2 (Prioridad baja):", seleccionar_pendientes(ordenes, "baja"))
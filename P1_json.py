import json

# Intento inicial con sintaxis inválida en JSON
texto_invalido = '{"codigo":"OS-001", "prioritaria":True, "fallas":["No enciende",]}'

print("--- INTENTO INICIAL ---")
try:
    datos = json.loads(texto_invalido)
    print(datos)
except json.JSONDecodeError as error:
    print("Error inicial capturado correctamente:")
    print(error)

# Texto con la sintaxis JSON corregida
texto_corregido = '{"codigo":"OS-001", "prioritaria":true, "fallas":["No enciende"]}'

print("\n--- TEXTO CORREGIDO ---")
datos = json.loads(texto_corregido)
print(f"codigo: {datos['codigo']} (Tipo: {type(datos['codigo']).__name__})")
print(f"prioritaria: {datos['prioritaria']} (Tipo: {type(datos['prioritaria']).__name__})")
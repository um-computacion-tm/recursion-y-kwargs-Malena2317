database = {
    1: {'nombres': 'Melina', 'apellidos': 'Navarro'},
    2: {'nombres': 'Ana','apellidos': 'Jimenez'},
    3: {'nombres': 'Milo', 'apellidos': 'Martínez'},
    4: {'nombres': 'Akira','apellidos': 'Lopez'}
}

def buscar_persona(nombres , apellidos):
    for id, persona in database.items():
        if persona['nombres'] == nombres and persona['apellidos'] == apellidos:
            return id
    return None
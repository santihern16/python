#Diccionarios

colores={"azul":"blue",
         "rojo":"red",
         "verde":"green",
         "amarillo":"yellow",
}
contactos={
        "Santiago":
        {"edad":22,"estatura":1.74},
        "Gaby":[18,1.65]
        }

print(contactos["Santiago"])
print(contactos.keys())
print(contactos.values())

colores ["azul"]="blau"
print(colores)
print(colores.keys())

equipo={
        30:"Messi", 
        11:"Neymar", 
        9:"Mbappe"
}

print(equipo[30])
print(equipo.get(12,"No existe un jugador con ese número")) #Primer parámetro: Clave. Segundo parámetro: Si no existe esa clave, agregar una excepción
print(equipo.values())
print(equipo.items())
print("Jugadores en el equipo: ")
print(len(equipo))
print(10 in equipo)
equipo.clear()
print(equipo)
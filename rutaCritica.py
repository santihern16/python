import networkx as nx
from datetime import datetime, timedelta

# Definimos las tareas, fechas de inicio y duración
tasks = {
    "Recolección de Requisitos": (datetime(2025, 4, 25), 3),
    "Diseño de la Arquitectura": (datetime(2025, 4, 28), 7),
    "Diseño de UI/UX": (datetime(2025, 4, 28), 5),
    "Configuración de Infraestructura": (datetime(2025, 5, 5), 4),
    "Desarrollo de Frontend móvil": (datetime(2025, 5, 5), 10),
    "Integración de Google Maps": (datetime(2025, 5, 15), 4),
    "Desarrollo de Backend": (datetime(2025, 5, 5), 8),
    "Integración Frontend-Backend": (datetime(2025, 5, 15), 5),
    "Pruebas funcionales y de desempeño": (datetime(2025, 5, 20), 5),
    "Ajustes finales y optimización": (datetime(2025, 5, 25), 3),
    "Entrega del MVP": (datetime(2025, 5, 28), 1),
}

# Crear el grafo dirigido
G = nx.DiGraph()

# Agregar nodos y duraciones
for task, (start, duration) in tasks.items():
    G.add_node(task, duration=duration)

# Definimos dependencias manualmente (muy importante para la ruta crítica)
dependencies = [
    ("Recolección de Requisitos", "Diseño de la Arquitectura"),
    ("Recolección de Requisitos", "Diseño de UI/UX"),
    ("Diseño de la Arquitectura", "Configuración de Infraestructura"),
    ("Configuración de Infraestructura", "Desarrollo de Frontend móvil"),
    ("Configuración de Infraestructura", "Desarrollo de Backend"),
    ("Desarrollo de Frontend móvil", "Integración de Google Maps"),
    ("Desarrollo de Backend", "Integración Frontend-Backend"),
    ("Integración de Google Maps", "Pruebas funcionales y de desempeño"),
    ("Integración Frontend-Backend", "Pruebas funcionales y de desempeño"),
    ("Pruebas funcionales y de desempeño", "Ajustes finales y optimización"),
    ("Ajustes finales y optimización", "Entrega del MVP"),
]

# Agregar las aristas al grafo
for dep in dependencies:
    G.add_edge(dep[0], dep[1])

# Encontrar la ruta crítica
critical_path = nx.dag_longest_path(G, weight='duration')

# Calcular la duración total
critical_duration = sum(G.nodes[task]['duration'] for task in critical_path)

# Mostrar resultados
print("Ruta crítica:")
for task in critical_path:
    print(f"- {task}")

print(f"\nDuración total de la ruta crítica: {critical_duration} días")

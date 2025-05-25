import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

# Definir dependencias
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

# Agregar aristas
for dep in dependencies:
    G.add_edge(dep[0], dep[1])

# Calcular la ruta crítica
critical_path = nx.dag_longest_path(G, weight='duration')

# Graficar el diagrama de Gantt + Ruta Crítica
fig, ax = plt.subplots(figsize=(14, 8))
yticks = []
ylabels = []
colors = []

# Construcción de barras para Gantt
for i, (task, (start, duration)) in enumerate(tasks.items()):
    end = start + timedelta(days=duration)
    color = 'tab:red' if task in critical_path else 'tab:blue'
    ax.barh(i, duration, left=start, height=0.5, color=color)
    yticks.append(i)
    ylabels.append(task)
    colors.append(color)

# Formato de fechas
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xticks(rotation=45)
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.set_xlabel("Fecha")
ax.set_title("Diagrama de Gantt con Ruta Crítica (CiudApp)")
ax.grid(True)

# Leyenda
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='tab:blue', label='Tarea'),
                   Patch(facecolor='tab:red', label='Ruta Crítica')]
ax.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.show()

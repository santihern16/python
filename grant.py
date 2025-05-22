import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Definimos las tareas, sus fechas de inicio y duración en días
tasks = [
    ("Recolección de Requisitos", datetime(2025, 4, 25), 3),
    ("Diseño de la Arquitectura", datetime(2025, 4, 28), 7),
    ("Diseño de UI/UX", datetime(2025, 4, 28), 5),
    ("Configuración de Infraestructura", datetime(2025, 5, 5), 4),
    ("Desarrollo de Frontend móvil", datetime(2025, 5, 5), 10),
    ("Integración de Google Maps", datetime(2025, 5, 15), 4),
    ("Desarrollo de Backend", datetime(2025, 5, 5), 8),
    ("Integración Frontend-Backend", datetime(2025, 5, 15), 5),
    ("Pruebas funcionales y de desempeño", datetime(2025, 5, 20), 5),
    ("Ajustes finales y optimización", datetime(2025, 5, 25), 3),
    ("Entrega del MVP", datetime(2025, 5, 28), 1),
]

# Creamos la figura
fig, ax = plt.subplots(figsize=(12, 6))

# Creamos el Gantt
for i, (task, start_date, duration) in enumerate(tasks):
    end_date = start_date + timedelta(days=duration)
    ax.barh(task, end_date - start_date, left=start_date, height=0.5)

# Configuración del eje de fechas
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.xticks(rotation=45)

# Títulos y etiquetas
plt.title('Diagrama de Gantt - Proyecto CiudApp')
plt.xlabel('Fecha')
plt.ylabel('Tareas')
plt.grid(True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
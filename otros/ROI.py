import matplotlib.pyplot as plt
import numpy as np

# Datos para los gráficos
metricas = ['Costo-Beneficio', 'ROI', 'Eficacia', 'Eficiencia', 'Efectividad']
valores = [1.3, 30, 10, 1.63, 100]

# Crear una figura grande con subgráficos
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Resultados de Evaluación del Proyecto', fontsize=20)

# Gráfico de Costo-Beneficio
axs[0, 0].barh(['Costo-Beneficio'], [valores[0]], color='skyblue')
axs[0, 0].set_xlim(0, 2)
axs[0, 0].set_title('Relación Costo-Beneficio')
axs[0, 0].grid(True)

# Gráfico de ROI
axs[0, 1].bar(['ROI'], [valores[1]], color='limegreen')
axs[0, 1].set_ylim(0, 100)
axs[0, 1].set_title('Retorno de Inversión (%)')
axs[0, 1].grid(True)

# Gráfico de Eficacia
axs[0, 2].bar(['Eficacia'], [valores[2]], color='gold')
axs[0, 2].set_ylim(0, 20)
axs[0, 2].set_title('Eficacia (%)')
axs[0, 2].grid(True)

# Gráfico de Eficiencia
axs[1, 0].bar(['Eficiencia'], [valores[3]], color='coral')
axs[1, 0].set_ylim(0, 2)
axs[1, 0].set_title('Índice de Eficiencia')
axs[1, 0].grid(True)

# Gráfico de Efectividad
axs[1, 1].bar(['Efectividad'], [valores[4]], color='orchid')
axs[1, 1].set_ylim(0, 120)
axs[1, 1].set_title('Efectividad (%)')
axs[1, 1].grid(True)

# Eliminar el sexto subplot vacío
fig.delaxes(axs[1, 2])

# Ajustar el layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# Análisis de la Tasa de Cambio del Dólar - API Gobierno Colombiano

Este proyecto contiene scripts para obtener y analizar datos de la tasa de cambio del dólar estadounidense (USD) contra el peso colombiano (COP) utilizando la API oficial del gobierno colombiano.

## Fuente de Datos

Los datos se obtienen de la API pública del gobierno colombiano:
- **URL**: https://www.datos.gov.co/resource/mcec-87by.json
- **Dataset**: Tasa Representativa del Mercado (TRM)
- **Formato**: JSON

## Archivos del Proyecto

### 1. `tasaDolar.py`
Script básico para obtener y mostrar datos de la tasa de cambio.

**Funcionalidades:**
- Obtención de datos desde la API
- Estadísticas básicas (valor actual, máximo, mínimo, promedio)
- Filtrado por fechas
- Visualización de datos recientes

**Uso:**
```bash
python tasaDolar.py
```

### 2. `analisis_tasa_dolar.py`
Script avanzado con análisis estadístico y visualizaciones.

**Funcionalidades:**
- Análisis estadístico detallado
- Gráficos de evolución temporal
- Promedios móviles (7 y 30 días)
- Distribución de valores
- Predicción simple basada en tendencia lineal
- Variación porcentual diaria

**Uso:**
```bash
python analisis_tasa_dolar.py
```

## Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **O instalar manualmente:**
```bash
pip install pandas sodapy requests matplotlib seaborn numpy
```

## Estructura de los Datos

Los datos obtenidos contienen los siguientes campos:

- **valor**: Tasa de cambio en pesos colombianos
- **unidad**: Moneda (COP)
- **vigenciadesde**: Fecha de inicio de vigencia
- **vigenciahasta**: Fecha de fin de vigencia

## Ejemplos de Uso

### Ejemplo 1: Obtener datos básicos
```python
from tasaDolar import obtener_tasa_dolar, mostrar_estadisticas

# Obtener datos
df = obtener_tasa_dolar(limite=1000)

# Mostrar estadísticas
mostrar_estadisticas(df)
```

### Ejemplo 2: Filtrar por fecha
```python
from tasaDolar import obtener_tasa_dolar, filtrar_por_fecha
from datetime import datetime, timedelta

df = obtener_tasa_dolar()

# Filtrar últimos 30 días
fecha_30d = datetime.now() - timedelta(days=30)
df_filtrado = filtrar_por_fecha(df, fecha_inicio=fecha_30d)
```

### Ejemplo 3: Análisis avanzado
```python
from analisis_tasa_dolar import obtener_datos_completos, analisis_estadistico_avanzado

df = obtener_datos_completos()
analisis_estadistico_avanzado(df)
```

## Características de los Scripts

### Script Básico (`tasaDolar.py`)
- ✅ Obtención de datos desde la API
- ✅ Conversión a DataFrame de pandas
- ✅ Estadísticas básicas
- ✅ Filtrado por fechas
- ✅ Manejo de errores

### Script Avanzado (`analisis_tasa_dolar.py`)
- ✅ Análisis estadístico completo
- ✅ Gráficos interactivos
- ✅ Promedios móviles
- ✅ Análisis de tendencias
- ✅ Predicción simple
- ✅ Visualización de distribución

## Notas Importantes

1. **Límites de la API**: La API tiene límites de consulta, por lo que se recomienda no hacer demasiadas consultas en poco tiempo.

2. **Datos históricos**: Los datos disponibles incluyen información histórica desde varios años atrás.

3. **Actualización**: Los datos se actualizan diariamente con la TRM oficial.

4. **Predicciones**: Las predicciones son estimaciones simples basadas en tendencias lineales y no deben usarse como base para decisiones financieras.

## Troubleshooting

### Error de conexión
Si tienes problemas de conexión, verifica:
- Tu conexión a internet
- Que la API esté disponible
- Que no hayas excedido los límites de consulta

### Error de dependencias
Si hay errores con las librerías:
```bash
pip install --upgrade pandas sodapy matplotlib seaborn numpy
```

### Error de visualización
Si los gráficos no se muestran:
- Asegúrate de tener un backend de matplotlib configurado
- En entornos sin GUI, usa: `plt.switch_backend('Agg')`

## Contribuciones

Si encuentras errores o quieres agregar funcionalidades, puedes:
1. Reportar issues
2. Proponer mejoras
3. Agregar nuevos análisis

## Licencia

Este proyecto es de uso libre y educativo. Los datos provienen de fuentes públicas del gobierno colombiano.


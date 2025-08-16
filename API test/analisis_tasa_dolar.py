#!/usr/bin/env python
# -*- coding: utf-8 -*-

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy
# pip install matplotlib
# pip install seaborn
# pip install numpy

import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo de gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def obtener_datos_completos():
    """
    Obtiene todos los datos disponibles de la tasa de cambio
    """
    try:
        client = Socrata("www.datos.gov.co", None)
        results = client.get("mcec-87by", limit=50000)  # Obtener más datos
        
        df = pd.DataFrame.from_records(results)
        df['vigenciadesde'] = pd.to_datetime(df['vigenciadesde'])
        df['vigenciahasta'] = pd.to_datetime(df['vigenciahasta'])
        df['valor'] = pd.to_numeric(df['valor'])
        
        # Ordenar por fecha
        df = df.sort_values('vigenciadesde')
        
        return df
    
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

def calcular_tendencias(df):
    """
    Calcula tendencias y patrones en los datos
    """
    if df is None or df.empty:
        return None
    
    # Calcular variación diaria
    df['variacion_diaria'] = df['valor'].diff()
    df['variacion_porcentual'] = (df['variacion_diaria'] / df['valor'].shift(1)) * 100
    
    # Calcular promedio móvil de 7 días
    df['promedio_movil_7d'] = df['valor'].rolling(window=7).mean()
    
    # Calcular promedio móvil de 30 días
    df['promedio_movil_30d'] = df['valor'].rolling(window=30).mean()
    
    return df

def graficar_evolucion_temporal(df, dias=365):
    """
    Grafica la evolución temporal de la tasa de cambio
    """
    if df is None or df.empty:
        print("No hay datos para graficar")
        return
    
    # Filtrar últimos N días
    fecha_limite = datetime.now() - timedelta(days=dias)
    df_filtrado = df[df['vigenciadesde'] >= fecha_limite].copy()
    
    if df_filtrado.empty:
        print(f"No hay datos para los últimos {dias} días")
        return
    
    # Calcular tendencias
    df_filtrado = calcular_tendencias(df_filtrado)
    
    # Crear figura
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Gráfico 1: Evolución del valor
    ax1.plot(df_filtrado['vigenciadesde'], df_filtrado['valor'], 
             label='Tasa de cambio', linewidth=1, alpha=0.7)
    ax1.plot(df_filtrado['vigenciadesde'], df_filtrado['promedio_movil_7d'], 
             label='Promedio móvil 7 días', linewidth=2, color='orange')
    ax1.plot(df_filtrado['vigenciadesde'], df_filtrado['promedio_movil_30d'], 
             label='Promedio móvil 30 días', linewidth=2, color='red')
    
    ax1.set_title(f'Evolución de la Tasa de Cambio USD/COP (Últimos {dias} días)', fontsize=14)
    ax1.set_ylabel('Pesos Colombianos (COP)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Variación porcentual
    ax2.plot(df_filtrado['vigenciadesde'], df_filtrado['variacion_porcentual'], 
             color='green', alpha=0.7, linewidth=1)
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax2.set_title('Variación Porcentual Diaria', fontsize=14)
    ax2.set_ylabel('Variación (%)', fontsize=12)
    ax2.set_xlabel('Fecha', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def analisis_estadistico_avanzado(df):
    """
    Realiza un análisis estadístico más detallado
    """
    if df is None or df.empty:
        print("No hay datos para analizar")
        return
    
    print("\n" + "="*60)
    print("ANÁLISIS ESTADÍSTICO AVANZADO")
    print("="*60)
    
    # Estadísticas descriptivas
    print("\nESTADÍSTICAS DESCRIPTIVAS:")
    print(f"Media: {df['valor'].mean():.2f} COP")
    print(f"Mediana: {df['valor'].median():.2f} COP")
    print(f"Desviación estándar: {df['valor'].std():.2f} COP")
    print(f"Coeficiente de variación: {(df['valor'].std() / df['valor'].mean()) * 100:.2f}%")
    print(f"Valor mínimo: {df['valor'].min():.2f} COP")
    print(f"Valor máximo: {df['valor'].max():.2f} COP")
    print(f"Rango: {df['valor'].max() - df['valor'].min():.2f} COP")
    
    # Análisis por períodos
    print("\nANÁLISIS POR PERÍODOS:")
    
    # Últimos 30 días
    fecha_30d = datetime.now() - timedelta(days=30)
    df_30d = df[df['vigenciadesde'] >= fecha_30d]
    if not df_30d.empty:
        print(f"Últimos 30 días - Promedio: {df_30d['valor'].mean():.2f} COP")
    
    # Últimos 90 días
    fecha_90d = datetime.now() - timedelta(days=90)
    df_90d = df[df['vigenciadesde'] >= fecha_90d]
    if not df_90d.empty:
        print(f"Últimos 90 días - Promedio: {df_90d['valor'].mean():.2f} COP")
    
    # Último año
    fecha_1a = datetime.now() - timedelta(days=365)
    df_1a = df[df['vigenciadesde'] >= fecha_1a]
    if not df_1a.empty:
        print(f"Último año - Promedio: {df_1a['valor'].mean():.2f} COP")

def graficar_distribucion(df):
    """
    Grafica la distribución de los valores de la tasa de cambio
    """
    if df is None or df.empty:
        print("No hay datos para graficar")
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Histograma
    ax1.hist(df['valor'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    ax1.axvline(df['valor'].mean(), color='red', linestyle='--', 
                label=f'Media: {df["valor"].mean():.2f}')
    ax1.axvline(df['valor'].median(), color='green', linestyle='--', 
                label=f'Mediana: {df["valor"].median():.2f}')
    ax1.set_title('Distribución de la Tasa de Cambio', fontsize=14)
    ax1.set_xlabel('Pesos Colombianos (COP)', fontsize=12)
    ax1.set_ylabel('Frecuencia', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Box plot
    ax2.boxplot(df['valor'], patch_artist=True, 
                boxprops=dict(facecolor='lightblue', alpha=0.7))
    ax2.set_title('Box Plot de la Tasa de Cambio', fontsize=14)
    ax2.set_ylabel('Pesos Colombianos (COP)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def predecir_tendencia_simple(df, dias_prediccion=7):
    """
    Predicción simple basada en tendencia lineal
    """
    if df is None or df.empty:
        print("No hay datos para predicción")
        return
    
    # Usar últimos 30 días para la predicción
    fecha_30d = datetime.now() - timedelta(days=30)
    df_reciente = df[df['vigenciadesde'] >= fecha_30d].copy()
    
    if len(df_reciente) < 10:
        print("No hay suficientes datos recientes para predicción")
        return
    
    # Crear variable temporal
    df_reciente['dias_desde_inicio'] = (df_reciente['vigenciadesde'] - df_reciente['vigenciadesde'].min()).dt.days
    
    # Ajuste lineal simple
    x = df_reciente['dias_desde_inicio'].values
    y = df_reciente['valor'].values
    
    # Calcular pendiente y intercepto
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)
    
    pendiente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    intercepto = (sum_y - pendiente * sum_x) / n
    
    # Predicción para los próximos días
    ultimo_dia = df_reciente['dias_desde_inicio'].max()
    dias_futuros = np.arange(ultimo_dia + 1, ultimo_dia + 1 + dias_prediccion)
    predicciones = pendiente * dias_futuros + intercepto
    
    print(f"\nPREDICCIÓN SIMPLE (próximos {dias_prediccion} días):")
    print(f"Tendencia: {'Al alza' if pendiente > 0 else 'A la baja'}")
    print(f"Cambio estimado por día: {pendiente:.2f} COP")
    
    for i, pred in enumerate(predicciones):
        fecha_pred = df_reciente['vigenciadesde'].max() + timedelta(days=i+1)
        print(f"Día {i+1} ({fecha_pred.strftime('%Y-%m-%d')}): {pred:.2f} COP")

def main():
    print("Iniciando análisis avanzado de la tasa de cambio del dólar...")
    
    # Obtener datos
    df = obtener_datos_completos()
    
    if df is not None:
        print(f"Datos obtenidos: {len(df)} registros")
        print(f"Período: {df['vigenciadesde'].min().strftime('%Y-%m-%d')} a {df['vigenciadesde'].max().strftime('%Y-%m-%d')}")
        
        # Análisis estadístico
        analisis_estadistico_avanzado(df)
        
        # Gráficos
        print("\nGenerando gráficos...")
        graficar_evolucion_temporal(df, 365)  # Último año
        graficar_distribucion(df)
        
        # Predicción simple
        predecir_tendencia_simple(df, 7)
        
    else:
        print("No se pudieron obtener los datos")

if __name__ == "__main__":
    main()


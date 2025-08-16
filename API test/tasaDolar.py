#!/usr/bin/env python
# -*- coding: utf-8 -*-

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy
# pip install requests

import pandas as pd
from sodapy import Socrata
import requests
from datetime import datetime, timedelta
import json

def obtener_tasa_dolar(limite=1000):
    """
    Obtiene los datos de la tasa de cambio del dólar desde la API del gobierno colombiano
    """
    try:
        # Cliente no autenticado para datos públicos
        client = Socrata("www.datos.gov.co", None)
        
        # Obtener datos de la API
        results = client.get("mcec-87by", limit=limite)
        
        # Convertir a DataFrame
        df = pd.DataFrame.from_records(results)
        
        # Convertir columnas de fecha
        df['vigenciadesde'] = pd.to_datetime(df['vigenciadesde'])
        df['vigenciahasta'] = pd.to_datetime(df['vigenciahasta'])
        df['valor'] = pd.to_numeric(df['valor'])
        
        # Ordenar por fecha (más reciente primero)
        df = df.sort_values('vigenciadesde', ascending=False)
        
        return df
    
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

def mostrar_estadisticas(df):
    """
    Muestra estadísticas básicas de la tasa de cambio
    """
    if df is None or df.empty:
        print("No hay datos para analizar")
        return
    
    print("\n" + "="*50)
    print("ESTADÍSTICAS DE LA TASA DE CAMBIO DEL DÓLAR")
    print("="*50)
    
    print(f"Período analizado: {df['vigenciadesde'].min().strftime('%Y-%m-%d')} a {df['vigenciadesde'].max().strftime('%Y-%m-%d')}")
    print(f"Total de registros: {len(df)}")
    print(f"\nValor actual (más reciente): {df.iloc[0]['valor']:.2f} COP")
    print(f"Valor más alto: {df['valor'].max():.2f} COP")
    print(f"Valor más bajo: {df['valor'].min():.2f} COP")
    print(f"Promedio: {df['valor'].mean():.2f} COP")
    print(f"Desviación estándar: {df['valor'].std():.2f} COP")

def filtrar_por_fecha(df, fecha_inicio=None, fecha_fin=None):
    """
    Filtra los datos por rango de fechas
    """
    if fecha_inicio:
        df = df[df['vigenciadesde'] >= fecha_inicio]
    if fecha_fin:
        df = df[df['vigenciadesde'] <= fecha_fin]
    
    return df

def mostrar_ultimos_dias(df, dias=30):
    """
    Muestra los datos de los últimos N días
    """
    fecha_limite = datetime.now() - timedelta(days=dias)
    df_filtrado = df[df['vigenciadesde'] >= fecha_limite]
    
    print(f"\nÚltimos {dias} días:")
    print(df_filtrado[['vigenciadesde', 'valor']].head(10))

def main():
    print("Obteniendo datos de la tasa de cambio del dólar...")
    
    # Obtener datos
    df = obtener_tasa_dolar(limite=2000)
    
    if df is not None:
        print(f"Datos obtenidos exitosamente: {len(df)} registros")
        
        # Mostrar primeros registros
        print("\nPrimeros 5 registros:")
        print(df[['vigenciadesde', 'valor', 'unidad']].head())
        
        # Mostrar estadísticas
        mostrar_estadisticas(df)
        
        # Mostrar últimos 30 días
        mostrar_ultimos_dias(df, 30)
        
        # Ejemplo de filtrado por fecha
        print("\n" + "="*50)
        print("EJEMPLO DE FILTRADO POR FECHA")
        print("="*50)
        
        # Últimos 7 días
        fecha_7_dias = datetime.now() - timedelta(days=7)
        df_7_dias = filtrar_por_fecha(df, fecha_inicio=fecha_7_dias)
        print(f"\nÚltimos 7 días ({len(df_7_dias)} registros):")
        print(df_7_dias[['vigenciadesde', 'valor']].head())
        
    else:
        print("No se pudieron obtener los datos")

if __name__ == "__main__":
    main()
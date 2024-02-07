#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:56:19 2024

@author: josepmencion
"""

import pandas as pd #Importamos la libreria Pandas para manipular y analizar datos. Diminutivo pd
archivo_excel = pd.ExcelFile('/Users/josepmencion/Downloads/Listados.xlsx') #Importamos Excel fuente de datos
#print(archivo_excel.sheet_names)



listado_general_df = pd.read_excel(archivo_excel, 'Listado General') #Leemos hoja Listado General y incluímos en márgen de datos listado_general_df
listado_notas_df = pd.read_excel(archivo_excel, 'Listado Notas') #Leemos hoja Listado Notas y incluímos en data frame listado_notas_df


#Ver primeras filas listado general
#print(listado_general_df.head())

#Ver primeras filas listado notas
#print(listado_notas_df.head())

listado_general_df.columns = listado_general_df.columns.str.strip()
listado_general_df['Email'] = listado_general_df['Email'].str.strip() #eliminamos espacios en los emails en hoja Listado General
alumnos = listado_general_df.to_dict(orient='records') #creamos diccionario a partir de los datos del Listado General y orient='records' -> lista de diccionarios
#print(alumnos) #ver diccionario alumnos

listado_notas_df.columns = listado_notas_df.columns.str.strip() #limpiamos los campos de espacios al inicio o final
listado_notas_df['Email'] = listado_notas_df['Email'].str.strip() #eliminamos espacios en los emails en hoja Listado Notas
listado_notas_dict = listado_notas_df.set_index('Email').to_dict(orient='index') #creamos diccionario con Listado Notas y orient='index' -> diccionario de diccionarios 
#print(listado_notas_dict) #ver diccionario alumnos

for alumno in alumnos:
    email = alumno['Email'].strip() #encontramos email alumno y borramos espacios inicio y final si es el caso
    if email in listado_notas_dict:#si se encuentra 
        alumno.update(listado_notas_dict[email])#actualizamos info notas alumno si lo hemos encontrado por mail

print(alumnos)

notas_quimica = [alumno['Nota de Química'] for alumno in alumnos if 'Nota de Química' in alumno]  #creamos lista alumnos quimica con nota
promedio_notas_quimica = sum(notas_quimica) / len(notas_quimica)  #calculamos media notas quimica
#print(promedio_notas_quimica) #Mostrar promedio notas de Química alumnos

nuevo_df = pd.DataFrame(alumnos)[['Apellido', 'Nombre', 'Nota de Física']]  #creamos márgen de datos con lista de diccionarios alumnos y selecciona nos quedamos con columnas 'Apellido' 'Nombre' y 'Nota de Física'
nuevo_df.to_excel('alumnos_fisica.xlsx', index=False)  #nuevo márgen de datos lo convertimos a nuevo archivo Excel 'alumnos_fisica.xlsx' sin incide del márgen de datos

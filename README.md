# gestion_alumnos
Programa para manejar calificaciones de alumnos con la librería Panda de Python
# Programa de Gestión de Alumnos

Este programa de Python está diseñado para facilitar la gestión de datos de alumnos a partir de un archivo Excel con dos hojas: "Listado General" y "Listado Notas". Permite combinar la información de ambas hojas en una sola estructura, calcular el promedio de las notas de Química de todos los alumnos y generar un nuevo archivo Excel con los apellidos, nombres y notas de Física de los alumnos.

## Características

- Lectura de datos desde un archivo Excel con múltiples hojas.
- Limpieza de espacios innecesarios en direcciones de email.
- Combinación de datos de listados generales y notas.
- Cálculo del promedio de notas de Química.
- Creación de un nuevo archivo Excel con datos específicos de los alumnos.

## Requisitos Previos

Para ejecutar este programa, necesitas tener Python y la biblioteca Pandas instalados en tu sistema. Este programa ha sido testeado con Python 3.8 y Pandas 1.2.4, pero debería ser compatible con versiones posteriores.

## Instalación

### Instalar Python

1. Descarga e instala la última versión de Python desde [python.org](https://www.python.org/downloads/).
2. Durante la instalación, asegúrate de marcar la opción "Add Python to PATH".

### Instalar Pandas

Abre una terminal y ejecuta el siguiente comando:
pip install pandas


## Uso

1. **Modifica la Ruta del Archivo Excel**: Antes de ejecutar el programa, edita el archivo `gestion_alumnos.py` para que apunte a la ubicación de tu archivo Excel. Busca la línea:

```python
archivo_excel = pd.ExcelFile('TU_RUTA/Listados.xlsx')

y reemplázala con la ruta correcta a tu archivo.

2. **Ejecuta el Programa**: Navega a la carpeta que contiene gestion_alumnos.py en una terminal y ejecuta:
python gestion_alumnos.py

3. **Revisa el Archivo Excel Generado:** Encuentra el archivo alumnos_fisica.xlsx en el mismo directorio del script. Este archivo contiene los datos procesados.

## Problemas Comunes y Soluciones
1. **Python/Pandas no encontrado:** Verifica que Python y Pandas estén correctamente instalados y accesibles desde la terminal.
2. **Archivo Excel no encontrado:** Asegúrate de que la ruta al archivo Excel en el script sea correcta.
3. **Permisos de escritura:** Verifica que tienes permisos de escritura en el directorio donde se ejecuta el script.

## Manejo de Espacios en los Datos
Este programa está diseñado para ser resistente a problemas comunes de formato en los datos de entrada, como los espacios innecesarios al principio o al final de los correos electrónicos y los nombres de las columnas en el archivo Excel. Utiliza la función .strip() de Python para limpiar estos campos automáticamente, asegurando así:

1. **Limpieza de Direcciones de Correo Electrónico:** Antes de procesar los datos, todas las direcciones de correo electrónico en las hojas "Listado General" y "Listado Notas" son limpiadas de espacios al principio y al final. Esto garantiza que las coincidencias entre las dos hojas se realicen correctamente, incluso si los datos originales contienen espacios accidentales.

2. **Limpieza de Nombres de Columnas:** Similarmente, los nombres de las columnas de ambos DataFrames son limpiados de espacios extra al principio y al final. Esto evita errores comunes al acceder a los datos por nombre de columna.

Estas medidas de limpieza permiten que el programa funcione correctamente incluso cuando los datos de entrada no están perfectamente formateados, proporcionando así una mayor flexibilidad y robustez.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. Si encuentras un error o tienes una sugerencia, por favor, abre un issue o un pull request.

## Licencia
Este proyecto está licenciado bajo Creative Commons. 

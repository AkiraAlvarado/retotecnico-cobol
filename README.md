# 📌 Proyecto: Procesador de Transacciones Bancarias

## 📖 Introducción
El propósito de este proyecto es procesar un archivo CSV que contiene registros de transacciones bancarias y generar un informe detallado con la siguiente información:

- El **balance final** de todas las transacciones.
- La **transacción de mayor monto registrada**.
- El **número total de transacciones** clasificadas por tipo (**Crédito** y **Débito**).

El proyecto está diseñado para manejar grandes volúmenes de datos de manera eficiente, utilizando la librería `pandas`.

---

## ⚙️ Instrucciones de Ejecución

### 1️⃣ Instalación de Dependencias
Antes de ejecutar el script, asegúrate de tener instalados los siguientes requisitos:
- **Python 3.x**
- **Pandas** (si no lo tienes instalado, usa el siguiente comando):

```bash
pip install pandas
```
## 1️⃣ Lectura de Datos con Pandas
Se utiliza `pd.read_csv()` para cargar los datos en un DataFrame, lo que permite manipular la información de manera eficiente. Esto es clave para trabajar con grandes volúmenes de datos, ya que pandas optimiza las operaciones de lectura y filtrado.

## 2️⃣ Cálculo de Sumas por Tipo de Transacción
Se filtran los valores donde `Tipo == "Crédito"` y `Tipo == "Débito"` para sumar los montos de cada categoría con `.sum()`. Esto permite calcular el balance final de forma rápida con la fórmula:

balance_final = suma_credito - suma_debito

## 3️⃣ Detección de la Transacción de Mayor Monto
Se usa `.idxmax()` para encontrar la fila con el monto más alto, lo que nos permite obtener la transacción con el monto más grande. Esto se hace en una sola pasada para optimizar el tiempo de ejecución.

## 4️⃣ Conteo de Transacciones
Se usa `.shape[0]` para contar cuántas transacciones hay de cada tipo (Crédito y Débito). Esto nos permite obtener el número total de operaciones realizadas en cada categoría.

## 5️⃣ Optimización y Escalabilidad

### Uso de Pandas
Pandas es una librería altamente optimizada para el manejo de grandes cantidades de datos, permitiendo realizar filtrados y operaciones matemáticas de manera eficiente en comparación con el uso de `csv` y bucles tradicionales.

### Cálculo Directo en Memoria
En lugar de iterar manualmente sobre cada fila del archivo CSV, se realizan los cálculos directamente en memoria utilizando las capacidades de pandas. De esta forma, se eliminan los bucles innecesarios y se procesan los datos de forma eficiente.

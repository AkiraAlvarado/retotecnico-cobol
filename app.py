import pandas as pd
import argparse

# Procesar transacciones y generar reporte
def procesar_transacciones(archivo_csv):
    # Leer el archivo CSV usando pandas
    df = pd.read_csv(archivo_csv)

    # Calcular el balance final
    suma_credito = df[df['Tipo'] == 'Crédito']['Monto'].sum()
    suma_debito = df[df['Tipo'] == 'Débito']['Monto'].sum()
    balance_final = suma_credito - suma_debito

    # Obtener la transacción de mayor monto
    transaccion_mayor = df.loc[df['Monto'].idxmax()]

    # Contar transacciones
    conteo_credito = df[df['Tipo'] == 'Crédito'].shape[0]
    conteo_debito = df[df['Tipo'] == 'Débito'].shape[0]

    # Mostrar el reporte
    print(f"Balance Final: {balance_final}")
    print(f"Transacción de Mayor Monto: ID {transaccion_mayor['ID']}, Monto {transaccion_mayor['Monto']}")
    print(f"Conteo de Transacciones: Crédito = {conteo_credito}, Débito = {conteo_debito}")

# Función principal para manejar los argumentos
def main():
    parser = argparse.ArgumentParser(description="Procesar transacciones bancarias y generar un reporte.")
    parser.add_argument('archivo', type=str, help="Ruta del archivo CSV con las transacciones bancarias.")
    
    args = parser.parse_args()
    procesar_transacciones(args.archivo)

# Ejecutar el script
if __name__ == '__main__':
    main()
import pandas as pd


def archivo(fichero, file):
    file.write(f'ANALISIS DE DATOS DEL FICHERO {fichero}\n')
    df = pd.read_csv(fichero, sep=',', encoding='LATIN1')

    nans = str(df.isna().sum().sum())
    file.write(f'Nans totales: {nans}\n')

    nulls = str(df.isnull().sum().sum())
    file.write(f'Nans totales: {nulls}\n')

    columnas = df.columns.values
    for colum in range(len(columnas)):
        nombre = columnas[colum]
        tipo_col = str(df[columnas[colum]].dtype)
        file.write(f'     La columna "{nombre}" es del tipo: {tipo_col}\n')


if __name__ == "__main__":

    file = open("analisis.txt", 'w')

    archivo('order_details.csv', file)
    file.write('\n')
    archivo('orders.csv', file)
    file.write('\n')
    archivo('data_dictionary.csv', file)
    file.write('\n')
    archivo('pizzas.csv', file)
    file.write('\n')
    archivo('pizza_types.csv', file)

    file.close()
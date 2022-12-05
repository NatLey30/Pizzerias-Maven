# Pizzerias-Maven
Se hace una predicción de los ingredientes a comprar para la siguiente semana, para lo cual cogemos la última semana del dataset y miramos cuantos ingredientes hacen falta.

Por otro lado, también se realiza un análisis de datos en los 5 archvios dados, en el que se obvserva cuantos nans y nulls hay, y de que tipo son cada columna.

Los ficheros de entrada son:
- orders.csv
- order_details.csv
- pizza_types.csv
- pizzas.csv
- data_dictionary.csv

Los ficheros de salida son:
- compra_semanal-csv
- analisis_archivos.txt

Los archivos de transformación son:
- compra.py
- analisis_datos-csv

Librerías
- pandas
- re

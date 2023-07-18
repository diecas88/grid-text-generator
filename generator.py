import math


separator = '|'
columns = 4
width_array = [10,20,70,10]
line_separator = '+'

#for twidth in width_array:
#    line_separator = line_separator + ('-' *twidth) + '+'

#print(line_separator)

rows_per_column_in_line = []

with open('/Users/diegoa/Documents/python_projects/grid text generator/raw.txt','r') as file:
    k = 0
    for line in file:
        #creamos el array para la linea
        rows_per_column_in_line.append([])
        #dividir la linea por el separador
        lines = line.split(separator)

        n = 0
        #empezar a calcular las filas para cada columna de la linea
        for textcol in lines:
            #divido el total del texto de la columna sobre el ancho dado y lo guardo en el array
            rows_per_column_in_line[k].append(math.ceil(len(textcol)/width_array[n]))
            
            n = n + 1

        k = k + 1    
        if(k>1):
            break
    
    #volvemos a leer el archivo para escribir 

    j = 0
    for line in file:
        #separamos las columnas de la linea
        lines = line.split(separator)
        #tomamos las maximas filas de las columnas
        maxrows = max(rows_per_column_in_line[j])




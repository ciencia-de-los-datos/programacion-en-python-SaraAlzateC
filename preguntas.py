"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    columna2 = [int(row[1]) for row in data]
    suma = sum(columna2)
    
    return suma


"""
    Retorne la suma de la segunda columna.

    
    Rta/
    214

    """
"return"


def pregunta_02():
    archivo = open('data.csv')
    lector = archivo.readlines()


    data = []
    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    columna1 = [row[0] for row in data]
    conteos = {}
    for letra in columna1:
        if letra in conteos:
            conteos[letra] += 1
        else:
            conteos[letra] = 1
    return [(letra, conteos[letra]) for letra in sorted(conteos)]
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """




def pregunta_03():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)
    result_dict = {}

    for row in data:
        if row[0] in result_dict:
            result_dict[row[0]] += int(row[1])
        else:
            result_dict[row[0]] = int(row[1])
    result = list(result_dict.items())
    result = sorted(result, key=lambda x: x[0])
    return result
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """


def pregunta_04():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    from collections import defaultdict

    counts = defaultdict(int)

    for row in data:
        year, month, day = row[2].split('-')
        counts[month] += 1
    result = sorted(counts.items())

    return(result)

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """


def pregunta_05():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    dicc_valores = {}
    for fila in data:
        letra = fila[0]
        valor = int(fila[1])
        if letra in dicc_valores:
            dicc_valores[letra].append(valor)
        else:
            dicc_valores[letra] = [valor]
    
    resultado = []
    for letra, valores in dicc_valores.items():
        max_val = max(valores)
        min_val = min(valores)
        resultado.append((letra, max_val, min_val))
    resultado = sorted(resultado, key=lambda x: x[0])
    return resultado

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """


def pregunta_06():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)
            
    dicc_valores = {}
    for fila in data:
        valores_col5 = fila[4].split(',')
        for valor in valores_col5:
            clave, val = valor.split(':')
            val = int(val)
            if clave in dicc_valores:
                dicc_valores[clave].append(val)
            else:
                dicc_valores[clave] = [val]
    resultado = []
    for clave, valores in dicc_valores.items():
        min_val = min(valores)
        max_val = max(valores)
        resultado.append((clave, min_val, max_val))
    resultado = sorted(resultado, key=lambda x: x[0])
    return resultado
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    numeros_por_letra = {}

    for sublista in data:
      letra = sublista[0]
      numero = int(sublista[1])
      if numero in numeros_por_letra:
        numeros_por_letra[numero].append(letra)
      else:
        numeros_por_letra[numero] = [letra]
    numeros_por_letra= dict(sorted(numeros_por_letra.items(), key=lambda item: item[0]))

    return numeros_por_letra

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

def pregunta_08():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    numeros_por_letra = {}

    for sublista in data:
        letra = sublista[0]
        numero = int(sublista[1])
        if numero in numeros_por_letra:
            numeros_por_letra[numero].add(letra)
        else:
            numeros_por_letra[numero] = {letra}
    numeros_por_letra = dict(sorted(numeros_por_letra.items(), key=lambda x: x[0]))
    return numeros_por_letra
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """


def pregunta_09():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    clave_count = {}

    for sublista in data:
        clave_string = sublista[4]
        pares_clave_valor = clave_string.split(',')
        for par in pares_clave_valor:
            clave = par.split(':')[0]
            if clave in clave_count:
                clave_count[clave] += 1
            else:
                clave_count[clave] = 1
        claves_ordenadas = sorted(clave_count.keys())
        clave_count_ordenado = {clave: clave_count[clave] for clave in claves_ordenadas}
    
    return clave_count_ordenado
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """


def pregunta_10():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    resultados = []

    for fila in data:
        letra = fila[0]
        elementos_col4 = len(set(fila[3].split(',')))
        elementos_col5 = len(fila[4].split(','))
        resultados.append((letra, elementos_col4, elementos_col5))

    return resultados
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """


def pregunta_11():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    conteo_letras_col4 = {}

    for fila in data:
        letras_col4 = fila[3].split(',')
        for letra in letras_col4:
            if letra in conteo_letras_col4:
                conteo_letras_col4[letra] += int(fila[1])
            else:
                conteo_letras_col4[letra] = int(fila[1])
    conteo_letras_col4 = dict(sorted(conteo_letras_col4.items(), key=lambda item: item[0]))
    return conteo_letras_col4
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """


def pregunta_12():
    archivo = open('data.csv')
    lector = archivo.readlines()
    data = []

    for linea in lector:
        fila = linea.strip().split('\t')
        data.append(fila)

    letra_suma_col5 = {}
    for fila in data:
        letra = fila[0]
        valores_col5 = [int(valor.split(':')[1]) for valor in fila[4].split(',')]
        suma_col5 = sum(valores_col5)
        if letra in letra_suma_col5:
            letra_suma_col5[letra] += suma_col5
        else:
            letra_suma_col5[letra] = suma_col5
    letra_suma_col5 = dict(sorted(letra_suma_col5.items(), key=lambda item: item[0]))
    return letra_suma_col5
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """












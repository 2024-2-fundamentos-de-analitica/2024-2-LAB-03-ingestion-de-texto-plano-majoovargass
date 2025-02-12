"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd
    import re
	
    inicio = dict()
    valores = []
    entrada = []
    with open('./files/input/clusters_report.txt') as file:
        for indicillo, line in enumerate(file):
            if indicillo < 4:
                # Catch header
                coincidenciasdeencabezado = re.finditer(r'\w+(?:\s\w+)*', line)
                for match in coincidenciasdeencabezado:
                    indicillo = match.start()
                    if indicillo not in inicio:
                        inicio[indicillo] = []
                    inicio[indicillo].append(match.group(0).lower())
            else:
                # Catch entry
                numerillodecoincidencias = re.findall(r'\d+,*\d?', line)
                if numerillodecoincidencias:
                    entrada = []
                    numerillos = [int(num) for num in numerillodecoincidencias[:2]] + [float(numerillodecoincidencias[2].replace(',', '.'))]
                    entrada += numerillos + ['']
                coincidenciasdetexto = re.findall(r'[a-zA-Z].+\n', line)
                if coincidenciasdetexto:
                    entrada[-1] += coincidenciasdetexto[0][:-1] + ' '
                else:
                    valores.append(entrada)
    
    encabezamiento = [' '.join(header_list) for header_list in inicio.values()]
    valores = list(map(lambda x: x[:-1] + [' '.join(x[-1].split()).replace('.', '')], valores))
    encabezamiento = list(map(lambda h: '_'.join(h.split()), encabezamiento))
    dfp = pd.DataFrame(valores, columns=encabezamiento)

    return dfp
print(pregunta_01())
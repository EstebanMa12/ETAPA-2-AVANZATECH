import csv
def read_csv(path):
    with open(path) as csvFile:
        reader = csv.reader(csvFile,delimiter=",")
        header = next(reader)
        listaDic = []
        for row in reader:
            iterable = zip(header,row)
            diccTemp = {key:value for (key,value) in iterable}
            listaDic.append(diccTemp)
        return listaDic
matriz = read_csv("./matches.csv")

#HACEMOS LA LECTURA DEL CSV y creamos una matriz de diccionarios que nos permita movernos entre la información

#ESCOGEMOS LOS MATCHES CON DURACION DE MENOS DE 1900 SEGUNDOS Y QUE SE DIERON EN NA1
filtrada = filter(lambda x: int(x["duration"])<1000 and x["platformid"]=="NA1",matriz)
try:
    while True:
        print(next(filtrada))
except StopIteration as error:
    pass

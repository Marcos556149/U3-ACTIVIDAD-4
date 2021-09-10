import csv
if __name__=='__main__':
    archivo=open('archivo.csv')
    reader=csv.reader(archivo,delimiter=';')

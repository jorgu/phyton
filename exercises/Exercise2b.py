# Hur många omgångar spelades säsongen 2019-2020 (osorterad csv)?

'''
   [0]   [1]    [2]     [3]        [4]         [5]        [6]       [7]    [8]   [9]
Säsong,Datum,Hemmalag,Bortalag,MålHemmalag,Målbortalag,Förlängning,Omgång,Plats,Publik
2019-2020,2019-09-20,Vara IBK,BK Halna,5,2,,1,"Alléhallen, Vara",132
2019-2020,2019-09-20,Skara IBK,Rydboholms SK,10,1,,1,"Vilanhallen, Skara",162
                        :
2019-2020,2020-03-07,Vara IBK,Falköpings IBK, 9, 0,X, 22,"Alléhallen, Vara",133
   [0]      [1]        [2]        [5]       [4][5][6][7]    [8]             [9]

'''
import csv

myFile = open('innebandyresultat-osorterad.csv',      # öppnar datafilen för läsning (streaming)
              'r', encoding='utf-8')        # och hanterar 'åäö'

myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var programmet  

omgångLista = []                            # initierar en tom lista (array)
for row in myDataReader:
    omgång = row[7]

    if omgång.isdigit():   # Vill inte räkna med rubriken, därför kollar jag att omgång är en siffra
        if not(omgång in omgångLista):
            omgångLista.append(omgång) # lägger till t ex omgång 6 till listan ['1', '9','2']
            
antalOmgångar = len(omgångLista)

print ('Antal spelade omgångar (datafil inte sorterade på "Omgång"): ' + str(antalOmgångar) + ' st')

myFile.close()                              # stänger filen efter läst klart

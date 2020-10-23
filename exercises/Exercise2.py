# Hur många omgångar spelades säsongen 2019-2020?

'''
   [0]   [1]    [2]     [3]        [4]         [5]        [6]       [7]    [8]   [9]
Säsong,Datum,Hemmalag,Bortalag,MålHemmalag,Målbortalag,Förlängning,Omgång,Plats,Publik
2019-2020,2019-09-20,Vara IBK,BK Halna,5,2,,1,"Alléhallen, Vara",132
2019-2020,2019-09-20,Skara IBK,Rydboholms SK,10,1,,1,"Vilanhallen, Skara",162
                        :
2019-2020,2020-03-07,Vara IBK,Falköpings IBK, 9, 0,X, 22,"Alléhallen, Vara",133
   [0]      [1]        [2]        [5]       [4][5][6][7]    [8]             [9]

'''


import csv                                  # importerar färdig kod som hanterar
                                            # lösning/skrivning av csv-fil

myFile = open('innebandyresultat.csv',      # öppnar datafilen för läsning (streaming)
              'r', encoding='utf-8')        # och hanterar 'åäö'

myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var programmet  
                                            # programmet befinner sig i filen, t ex vilken rad
antalOmgångar       = 0
senastSparadeOmgång = ''

for row in myDataReader:
    omgång = row[7]

    # denna kod utnyttjar att matcherna kommer sorterat på omgång
    if omgång.isdigit():   # Vill inte räkna med rubriken, därför kollar jag att omgång är en siffra
        if omgång != senastSparadeOmgång:
            antalOmgångar = antalOmgångar + 1
            senastSparadeOmgång = omgång

print ('Antal spelade omgångar: ' + str(antalOmgångar) + ' st')

myFile.close()                              # stänger filen efter man läst klart


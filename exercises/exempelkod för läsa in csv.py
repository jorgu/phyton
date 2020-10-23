# file: exempelkod för läsa in csv.py

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

myFile = open('innebandyresultat.csv',      # öppnar datafilen för läsning
              'r', encoding='utf-8')        # och hanterar 'åäö'
myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var  
                                            # programmet befinner sig i filen, t ex vilken rad


print ('läser in och skriver ut kolumnerna via index!')

for row in myDataReader:    # är en iteration som pågår till itererat igenom alla filrader
    
# läser in värden i namngivna variabler för förenkla men behövs inte
    säsong      = row[0]  # läser in första kolumnen i raden i egen variabel
    speldag     = row[1]  # läser in datum i variabeln 'speldag'
    hemmalag    = row[2]
    bortalag    = row[3]
    målHemmalag = row[4]
    målBortalag = row[5]
    förlängning = row[6]
    omgång      = row[7]
    plats       = row[8]
    publik      = row[9]

    print (säsong, speldag, hemmalag, bortalag, målHemmalag, målBortalag
           , förlängning, omgång, plats, publik)

myFile.close()

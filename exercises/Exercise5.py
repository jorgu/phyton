# 12 lag spelade säsongen 2019-2020, vilka?

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

myFile = open('innebandyresultat.csv',      # öppnar datafilen för läsning (streaming)
              'r', encoding='utf-8')        # och hanterar 'åäö'

myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var programmet  
                                            # programmet befinner sig i filen, t ex vilken rad
identifieradeLag  = []

for row in myDataReader:
    if row[4].isdigit():                    # ignorerar rubrikraden
        hemmalag = row[2]
        bortalag = row[3]

        if not(hemmalag in identifieradeLag):
            identifieradeLag.append(hemmalag)

        if not(bortalag in identifieradeLag):
            identifieradeLag.append(bortalag)

                
print ('Dessa lag spelade säsongen 2019/2020: ')
for lag in identifieradeLag:
       print(lag)

myFile.close()                              # stänger filen efter läst klart

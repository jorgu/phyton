# Hur många matcher spelades under säsongen 2019-2020?

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
antalMatcher = 0

for row in myDataReader:
    målHemmalag = row[4]

    if målHemmalag.isdigit():
        målHemmalag = int(målHemmalag)
        if målHemmalag >= 0:
            antalMatcher = antalMatcher + 1
                
print ('Antal spelade matcher är ' + str(antalMatcher) + ' st')

myFile.close()                              # stänger filen efter läst klart

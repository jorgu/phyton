# Hur många poäng fick Skara IBK säsongen 2019-2020?

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
                                            
lagMedMestPoäng = {                         # en dictionary som håller reda på lag med
    'lagnamn': '',                          # mest poäng jus nu
    'poäng': 0
}

kolladeLag      = []                        # Håller reda på vilka lag som är räknade
totalpoäng      = 0

for row in myDataReader:
    if row[4].isdigit():                    # ignorerar rubrikraden
        hemmalag    = row[2]
        bortalag    = row[3]
        målHemmalag = int(row[4])
        målBortalag = int(row[5])
        förlängning = row[6]

        if not(hemmalag in kolladeLag):
            totalpoäng = 0
            totalpoäng = beräknaLagpoäng (hemmalag, målHemmalag, målBortalag, förlängning)

        kolladeLag.append(hemmalag)
        if totalpoäng > lagMedMestPoäng['poäng']:
            lagMedMestPoäng['lagnamn'] = hemmalag
            lagMedMestPoäng['poäng']   = totalpoäng
            print(lagMedMestPoäng['lagnamn'] + ': ' + str(lagMedMestPoäng['poäng']))
                      
print (lagMedMestPoäng['lagnamn'] + ' fick ' + str(lagMedMestPoäng['poäng']) + ' poäng')

myFile.close()                              # stänger filen efter läst klart


def beräknaLagpoäng(lag, målHemma, målBorta, förlängning):
     
    if förlängning == 'X':
        vinst    = 2
        oavgjort = 1
        förlust  = 1
    else:
        vinst    = 3
        förlust  = 0 


    if målHemmalag > målBortalag:          
        totalpoäng = totalpoäng + vinst
    elif målHemmalag == målBortalag:
        totalpoäng = totalpoäng + oavgjort
    else:       # underförstått förlust
        totalpoäng = totalpoäng + förlust
        
    if målHemmalag < målBortalag:          
        totalpoäng = totalpoäng + vinst
    elif målHemmalag == målBortalag:
        totalpoäng = totalpoäng + oavgjort
    else:       # underförstått förlust
        totalpoäng = totalpoäng + förlust        

    return totalpoäng

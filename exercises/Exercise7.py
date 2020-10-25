# Vilket lag vann säsongen 2019-2020?


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
import allaLagISerien

myFile = open('innebandyresultat.csv',      # öppnar datafilen för läsning (streaming)
              'r', encoding='utf-8')        # och hanterar 'åäö'

myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning (genom en pekare)   
                                            # var programmet befinner sig i filen, t ex vilken rad
                                            

allaLag = allaLagISerien.getAllTeams(myDataReader)  # får en array med alla lag i serien från filen
myFile.seek(0)                                      # filpekare ställs om till att peka på första post i filen igen

lagMedMestPoäng = {                         # en dictionary som håller reda på lag med
    'lagnamn': '',                          # mest poäng jus nu
    'poäng': 0
}


for lag in allaLag:
    totalpoäng = 0

    for row in myDataReader:

        if row[4].isdigit():                # ignorerar rubrikraden
            hemmalag    = row[2]
            bortalag    = row[3]
            målHemmalag = int(row[4])
            målBortalag = int(row[5])
            förlängning = row[6]

            if hemmalag == lag:
                aktuellalagetsMål   = målHemmalag
                motståndarlagetsMål = målBortalag
                totalpoäng = totalpoäng + allaLagISerien.beräknaLagpoäng (aktuellalagetsMål, motståndarlagetsMål, förlängning)

            if bortalag == lag:
                aktuellalagetsMål   = målBortalag
                motståndarlagetsMål = målHemmalag
                totalpoäng = totalpoäng + allaLagISerien.beräknaLagpoäng (aktuellalagetsMål, motståndarlagetsMål, förlängning)
            
    if totalpoäng > lagMedMestPoäng['poäng']:
        lagMedMestPoäng['lagnamn'] = lag
        lagMedMestPoäng['poäng']   = totalpoäng

    myFile.seek(0)                          # itererat igenom hela filen, börjar om i datafilen genom att ställa
                                            # om pekare till första raden i filen inför nästa lag. 

myFile.close()                              # stänger filen efter läst klart

print (lagMedMestPoäng["lagnamn"] + ' vann serien och fick ' + str(lagMedMestPoäng['poäng']) + ' poäng')


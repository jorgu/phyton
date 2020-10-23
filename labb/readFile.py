import csv                                  # importerar färdig kod som hanterar
                                            # lösning/skrivning av csv-fil
'''
myFile = open('innebandyresultat.csv', 'r') # öppnar datafilen för läsning
myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var  
                                            # programmet befinner sig i filen, t ex vilken rad


print ('läser in och skriver ut kolumnerna via index!')

for row in myDataReader:
    säsong      = row[0]
    speldag     = row[1]
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

'''
'''
• Hur många matcher spelades säsongen 2019-2020?
• Hur många omgångar spelades säsongen 2019-2020?
  o Hur många omgångar spelades säsongen 2019-2020 (osorterad csv)?
• Hur många matcher spelade lag X säsongen 2019-2020?
• Hur många poäng fick Skara IBK säsongen 2019-2020
• Hur många lag spelade säsongen 2019-2020?
• Vilket lag vann serien säsongen 2019-2020?


'''

# Hur många matcher?

myFile = open('innebandyresultat.csv', 'r') # öppnar datafilen för läsning
myDataReader = csv.reader(myFile)           # skapar en variabel som håller ordning var programmet  
                                            # programmet befinner sig i filen, t ex vilken rad
antalMatcher = 0

for row in myDataReader:
    säsong      = row[0]
    speldag     = row[1]
    hemmalag    = row[2]
    bortalag    = row[3]
    målHemmalag = row[4]
    målBortalag = row[5]
    förlängning = row[6]
    omgång      = row[7]
    plats       = row[8]
    publik      = row[9]

    if målHemmalag.isdigit():
        målHemmalag = int(målHemmalag)
        if målHemmalag >= 0:
            antalMatcher = antalMatcher + 1
                
print ('Antal spelade matcher är ' + str(antalMatcher) + ' st')

myFile.close()

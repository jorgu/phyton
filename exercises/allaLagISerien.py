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
def getAllTeams(inDataReader):

    lagLista = []

    for row in inDataReader:
        if row[4].isdigit():    
            hemmalag = row[2]
            bortalag = row[3]

            if not(hemmalag in lagLista):
                lagLista.append(hemmalag)

            if not(bortalag in lagLista):
                lagLista.append(bortalag)
    
    return lagLista


######################################################################################


def beräknaLagpoäng(lagetsMål, motståndarensMål, förlängning):
     
    if förlängning == 'X':
        vinst    = 2
        oavgjort = 1
        förlust  = 1
    else:
        vinst    = 3
        förlust  = 0 


    if lagetsMål > motståndarensMål:          
        poäng = vinst
    elif lagetsMål == motståndarensMål:
        poäng = oavgjort
    else:       # underförstått förlust
        poäng = förlust
        
    return poäng


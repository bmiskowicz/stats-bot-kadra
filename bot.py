#libraries required to scrap the data
from pyparsing import Char
from selenium import webdriver
from selenium.webdriver.common.by import By


#libraries required to save the .xlxs image
import numpy as np
import pandas as pd
import time
import dataframe_image as dfi


          
#empty arrays just to make table in .png prettier
emptyA = np.empty((15), dtype=Char)
for i in range(15):
    emptyA[i] = '|'
emptyB = np.empty((15), dtype=Char)
for i in range(15):
    emptyB[i] = '|'

#tables for players numbers, positions, names and statistics
numbersA = np.zeros((24, 15))

posA = np.empty((24, 15), dtype="S2")

playersA = np.empty((24, 15), dtype="S18")

teamA = np.zeros((24, 15, 18))


#putting additional data, so array doesn't have random values in empty spots
#tables have to have specified size, so they can be transformed into dataframe (which is used to convert self into .csv image)
for team in range(24):
    playersA[team, 14] = " "
    posA[team, 14] = " "
    numbersA[team, 14] = 0
    
    playersA[team, 14] = "lacznie"


#lists of teams and matches
teamslist = ['Poland', 'Brazil', 'France', 'Türkiye', 'Netherlands', 'Tunisia', 'United States', 'Slovenia', 'Cuba', 'Italy', 'Serbia', 'Iran', 'Germany', 'Japan', 'Argentina', 'Ukraine', 'Bulgaria',
            'Canada', 'Qatar', 'Cameroon', 'Puerto Rico', 'Egypt', 'Mexico', 'China']
matcheslist = ['13455', '13456', '13468']

for match in matcheslist:

    #getting the link
    link = "https://en.volleyballworld.com/volleyball/competitions/vnl-2022/schedule/" + match + "/#boxscore"
    #query to get data from particular set or all sets
    query = "div[class='vbw-o-table-wrap'] table[class*='vbw-set-" + "all" + "'] td[class*='vbw-o-table__cell']"
    
    #driver needed to open the browser
    driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe')

    #opening the link in the browser
    driver.get(link)
    time.sleep(5)
    

    #getting the teams names
    team = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-wrapper vbw-stats-by-player-wrapper'] div[class='vbw-mu__team__name']")
    name1 = team[0].get_attribute("textContent")
    name2 = team[1].get_attribute("textContent")
    index1 = teamslist.index(name1)
    index2 = teamslist.index(name2)
    
    #scrapping the data from all tables
    web_element = driver.find_elements(By.CSS_SELECTOR, query)

    #getting the teams players positions, numbers, names and first stats
    if numbersA[index1, 0] == 0: 
        #if its the first time this team is scrapped
        for player in range(14):
            #auxiliary variable, it will be used in whole function
            pom2 = player*9 

            numbersA[index1, player] = (web_element[pom2].get_attribute("textContent"))
            playersA[index1, player] = (web_element[1 + pom2].get_attribute("textContent")).encode('ascii', 'ignore').decode('utf-8')
            posA[index1, player] = (web_element[2 + pom2].get_attribute("textContent")).encode('ascii', 'ignore').decode('utf-8')
            teamA[index1, player, 0] = (web_element[3 + pom2].get_attribute("textContent"))
            
    else:
        for player in range(14):
            pom2 = player*9 
            result = ((np.where(float(web_element[0 + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]

            teamA[index1, result, 0] = teamA[index1, result, 0] + float((web_element[3 + pom2].get_attribute("textContent")))


    #getting the teams players positions, numbers, names and first stats
    if numbersA[index2, 0] == 0: 
        #if its the first time this team is scrapped
        for player in range(14):
            #auxiliary variable, it will be used in whole function
            pom2 = player*9
            numbersA[index2, player] = (web_element[784 + pom2].get_attribute("textContent"))
            playersA[index2, player] = (web_element[784 + 1 + pom2].get_attribute("textContent")).encode('ascii', 'ignore').decode('utf-8')
            posA[index2, player] = (web_element[784 + 2 + pom2].get_attribute("textContent")).encode('ascii', 'ignore').decode('utf-8')
            teamA[index2, player, 0] = (web_element[784 + 3 + pom2].get_attribute("textContent"))
            
    else:
        for player in range(14):
            pom2 = player*9 
            result = ((np.where(float(web_element[784 + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]

            teamA[index2, result, 0] = teamA[index2, result, 0] + float((web_element[784 + 3 + pom2].get_attribute("textContent")))
            



    #TEAM A
    #attack 126
    pom = 126
    for player in range(14):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]
        
        teamA[index1, result, 11] = teamA[index1, result, 11] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index1, result, 10] = teamA[index1, result, 10] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        teamA[index1, result, 9] =  teamA[index1, result, 9] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))
        if(teamA[index1, result, 9] == 0):   
            teamA[index1, result, 12] = 0
            teamA[index1, result, 13] = 0
        else:   
            teamA[index1, result, 12] = "{:.2f}".format(float(teamA[index1, result, 11]*100/teamA[index1, result, 9]))
            teamA[index1, result, 13] = "{:.2f}".format(float((teamA[index1, result, 11]-teamA[index1, result, 10])*100 / teamA[index1, result, 9]))


    #block 238
    pom = 238
    for player in range(14):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]
        
        teamA[index1, result, 14] = teamA[index1, result, 14] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index1, result, 15] = teamA[index1, result, 15] + float((web_element[pom + 5 + pom2].get_attribute("textContent")))


    #service 350
    pom = 350
    for player in range(14):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]
        
        teamA[index1, result, 4] = teamA[index1, result, 4] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index1, result, 3] = teamA[index1, result, 3] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        teamA[index1, result, 2] = teamA[index1, result, 2] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))
        if(teamA[index1, result, 2] == 0 or web_element[pom + 7 + pom2].get_attribute("textContent") == ''):   
            teamA[index1, result, 5] = 0
        else:  
            teamA[index1, result, 5] = "{:.2f}".format(float((teamA[index1, result, 4] - teamA[index1, result, 3])*100/teamA[index1, result, 2]))


    #reception 462
    pom = 462
    for player in range(14):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]

        teamA[index1, result, 6] = teamA[index1, result, 6] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))
        teamA[index1, result, 17] = teamA[index1, result, 17] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index1, result, 7] = teamA[index1, result, 7] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        if(teamA[index1, result, 6] == 0):   
            teamA[index1, result, 8] = 0
        else:  
            teamA[index1, result, 8] = "{:.2f}".format(float(teamA[index1, result, 17]*100/teamA[index1, result, 6]))
        
        #balance
        teamA[index1, result, 1] = teamA[index1, result, 0] - teamA[index1, result, 3] - teamA[index1, result, 7] - teamA[index1, result, 10]


    #digs 574
    pom = 574
    for player in range(14):
        pom2 = player*7
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index1, :]))[0])[0]

        teamA[index1, result, 16] = teamA[index1, result, 16] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))





    #TEAM B
    #attack
    pom = 910
    #pom = 9*14 + 784
    for player in range(14):
        pom2 = player*8
        #result = ((np.where(float(web_element[910 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]
        
        teamA[index2, result, 11] = teamA[index2, result, 11] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index2, result, 10] = teamA[index2, result, 10] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        teamA[index2, result, 9] = teamA[index2, result, 9] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))

        if(teamA[index2, result, 9] == 0):   
            teamA[index2, result, 12] = 0
            teamA[index2, result, 13] = 0
        else:   
            teamA[index2, result, 12] = "{:.2f}".format(float(teamA[index2, result, 11]*100/teamA[index2, result, 9]))
            teamA[index2, result, 13] = "{:.2f}".format(float((teamA[index2, result, 11]-teamA[index2, result, 10])*100 / teamA[index2, result, 9]))


    #block
    pom = 1022   
    for player in range(14):
        pom2 = player*8
        #result = ((np.where(float(web_element[1022 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]
        
        teamA[index2, result, 14] = teamA[index2, result, 14] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index2, result, 15] = teamA[index2, result, 15] + float((web_element[pom + 5 + pom2].get_attribute("textContent")))


    #service
    pom = 1134
    for player in range(14):
        pom2 = player*8
        #result = ((np.where(float(web_element[1134 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]
        
        teamA[index2, result, 4] = teamA[index2, result, 4] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index2, result, 3] = teamA[index2, result, 3] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        teamA[index2, result, 2] = teamA[index2, result, 2] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))
        if(teamA[index2, result, 2] == 0 or web_element[pom + 7 + pom2].get_attribute("textContent") == ''):   
            teamA[index2, result, 5] = 0
        else:  
            teamA[index2, result, 5] = "{:.2f}".format(float((teamA[index2, result, 4] - teamA[index2, result, 3])*100/teamA[index2, result, 2]))


    #reception
    pom = 1246
    for player in range(14):
        pom2 = player*8
        #result = ((np.where(float(web_element[1246 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]
        
        teamA[index2, result, 6] = teamA[index2, result, 6] + float((web_element[pom + 6 + pom2].get_attribute("textContent")))
        teamA[index2, result, 17] = teamA[index2, result, 17] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))
        teamA[index2, result, 7] = teamA[index2, result, 7] + float((web_element[pom + 4 + pom2].get_attribute("textContent")))
        if(teamA[index2, result, 6] == 0):   
            teamA[index2, result, 8] = 0
        else:  
            teamA[index2, result, 8] = "{:.2f}".format(float(teamA[index2, result, 17]*100/teamA[index2, result, 6]))

        #point balance
        teamA[index2, result, 1] = teamA[index2, result, 0] - teamA[index2, result, 3] - teamA[index2, result, 7] - teamA[index2, result, 10]


    #digs
    pom = 1358
    for player in range(14):
        pom2 = player*7
        #result = ((np.where(float(web_element[1358 + player*7].get_attribute("textContent")) == numbersA))[0])[0]
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA[index2, :]))[0])[0]

        teamA[index2, result, 16] = teamA[index2, result, 16] + float((web_element[pom + 3 + pom2].get_attribute("textContent")))


#decoding strings, cause names are in different languages
posA = np.char.decode(posA, encoding="utf-8", errors='ignore')
playersA = np.char.decode(playersA, encoding="utf-8", errors='ignore')



#team stats
thislist = [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 14, 15, 16, 17]


#calculating the teams stats
for team in range(24):
    for player in range(14):
        for el in thislist:
            teamA[team, 14, el] = teamA[team, 14, el] + teamA[team, player, el]


    #saving the teams reception
    if(teamA[team, 14, 6] == 0):   teamA[team, 14, 8] = 0
    else:   teamA[team, 14, 8] = "{:.2f}".format(float(teamA[team, 14, 17]*100/teamA[team, 14, 6]))

    #saving the teams service eff%
    if(teamA[team, 14, 2] == 0):   teamA[team, 14, 5] = 0
    else:   teamA[team, 14, 5] = "{:.2f}".format(float((teamA[team, 14, 4] - teamA[team, 14, 3])*100 / teamA[team, 14, 2]))

    #saving the teams attack efficiency%
    if(teamA[team, 14, 9] == 0):   teamA[team, 14, 12] = 0
    else:   teamA[team, 14, 12] = "{:.2f}".format(float(teamA[team, 14, 11]*100 / teamA[team, 14, 9]))

    #saving the teams attack effectivity%
    if(teamA[team, 14, 9] == 0):   teamA[team, 14, 13] = 0
    else:   teamA[team, 14, 13] = "{:.2f}".format(float((teamA[team, 14, 11] - teamA[team, 14, 10])*100 / teamA[team, 14, 9]))

A = pd.DataFrame({'Nazwisko':playersA[1, :], 'Pozycja':posA[1, :], ' ':emptyA, 'Suma PKT':teamA[1, :,0].astype(int), 'Bilans':teamA[1, :,1].astype(int), ' ':emptyA, 'Zagrywki':teamA[1, :,2].astype(int),
    'Błędy':teamA[1, :,3].astype(int), 'Asy':teamA[1, :,4].astype(int), 'Eff %':teamA[1, :,5], ' ':emptyA, 'Przyjęcia':teamA[1, :,6].astype(int), 'Błędów':teamA[1, :,7].astype(int),
    'Perf%':teamA[1, :,8], ' ':emptyA, 'Ataki':teamA[1, :,9].astype(int), 'Bł/Bl':teamA[1, :,10].astype(int), 'Pkt':teamA[1, :,11].astype(int), 'Skut%':teamA[1, :,12],
    'Eff%':teamA[1, :,13], ' ':emptyA, 'Bloki':teamA[1, :,14].astype(int), 'Wybloki':teamA[1, :,15].astype(int), ' ':emptyA, 'Obrony':teamA[1, :,16].astype(int), ' ':emptyA, 'Przyj. pos':teamA[1, :,17].astype(int)},
    columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony', ' ', 'Przyj. pos']).set_index(numbersA[1, :].astype(int))

"""
#transform into dataframe
A = pd.DataFrame({'Nazwisko':playersA, 'Pozycja':posA, ' ':emptyA, 'Suma PKT':teamA[:,0].astype(int), 'Bilans':teamA[:,1].astype(int), ' ':emptyA, 'Zagrywki':teamA[:,2].astype(int),
    'Błędy':teamA[:,3].astype(int), 'Asy':teamA[:,4].astype(int), 'Eff %':teamA[:,5], ' ':emptyA, 'Przyjęcia':teamA[:,6].astype(int), 'Błędów':teamA[:,7].astype(int),
    'Perf%':teamA[:,8], ' ':emptyA, 'Ataki':teamA[:,9].astype(int), 'Bł/Bl':teamA[:,10].astype(int), 'Pkt':teamA[:,11].astype(int), 'Skut%':teamA[:,12],
    'Eff%':teamA[:,13], ' ':emptyA, 'Bloki':teamA[:,14].astype(int), 'Wybloki':teamA[:,15].astype(int), ' ':emptyA, 'Obrony':teamA[:,16].astype(int)},
    columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersA)

B = pd.DataFrame({'Nazwisko':playersA, 'Pozycja':posA, ' ':emptyB, 'Suma PKT':teamA[:,0].astype(int), 'Bilans':teamA[:,1].astype(int), ' ':emptyB, 'Zagrywki':teamA[:,2].astype(int),
    'Błędy':teamA[:,3].astype(int), 'Asy':teamA[:,4].astype(int), 'Eff %':teamA[:,5], ' ':emptyB, 'Przyjęcia':teamA[:,6].astype(int), 'Błędów':teamA[:,7].astype(int),
    'Perf%':teamA[:,8], ' ':emptyB, 'Ataki':teamA[:,9].astype(int), 'Bł/Bl':teamA[:,10].astype(int), 'Pkt':teamA[:,11].astype(int), 'Skut%':teamA[:,12],
    'Eff%':teamA[:,13], ' ':emptyB, 'Bloki':teamA[:,14].astype(int), 'Wybloki':teamA[:,15].astype(int), ' ':emptyB, 'Obrony':teamA[:,16].astype(int)},
    columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersA)

"""


#exporting dataframes to .png images
#nameA = match + '_' + set + '_' + 'A.png'      
#nameB = match + '_' + set + '_' + 'B.png'
dfi.export(A, "test.png")
#   dfi.export(B, nameB)

driver.close()




###########
# dodać poprawne przyjęcia i poprawić % przyjęcia zagrywki, bo jest obliczane z poprawnych przyjęć z jednego meczu
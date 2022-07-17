from pyparsing import Char
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time
import numpy as np
import pandas as pd
import dataframe_image as dfi


def fetch(match, set):
    link = "https://en.volleyballworld.com/volleyball/competitions/vnl-2022/schedule/" + match + "/#boxscore"

    query = "div[class='vbw-o-table-wrap'] table[class*='vbw-set-" + set + "'] td[class*='vbw-o-table__cell']"


    #op = webdriver.ChromeOptions()
    #op.add_argument('headless')
    #driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe', options=op)
    #driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    driver.get(link)

    playerOneB = driver.find_element(By.XPATH, '//table[@data-team="teamb" and @data-set="' + set + '"]//td[@class="vbw-o-table__cell playername"]')
    playerOneB = playerOneB.get_attribute("textContent")


    team = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-wrapper vbw-stats-by-player-wrapper'] div[class='vbw-mu__team__name']")

    name1 = team[0].get_attribute("textContent")
    name2 = team[1].get_attribute("textContent")


    web_element = driver.find_elements(By.CSS_SELECTOR, query)

    for i in range(0, len(web_element)):
        if (web_element[i].get_attribute("textContent")) == playerOneB:
            startB = i-1
            break

    graczyB = int((len(web_element)-startB)/56)
    graczyA = int(len(web_element)/56) - graczyB
    

    emptyA = np.empty((graczyA+1), dtype=Char)
    for i in range(graczyA+1):
        emptyA[i] = '|'

    emptyB = np.empty((graczyB+1), dtype=Char)
    for i in range(graczyB+1):
        emptyB[i] = '|'


    numbersA = np.empty((graczyA+1), dtype=int)
    numbersB = np.empty((graczyB+1), dtype=int)

    posA = np.empty(graczyA+1, dtype="S2")
    posB = np.empty(graczyB+1, dtype="S2")

    playersA = np.empty(graczyA+1, dtype="S18")
    playersB = np.empty(graczyB+1, dtype="S18")

    teamA = np.zeros((graczyA+1, 17))
    teamB = np.zeros((graczyB+1, 17))


    for player in range(graczyA):
        pom2 = player*9
        numbersA[player] = (web_element[pom2].get_attribute("textContent"))
        playersA[player] = (web_element[1 + pom2].get_attribute("textContent")).encode()
        posA[player] = (web_element[2 + pom2].get_attribute("textContent")).encode()
        teamA[player, 0] = (web_element[3 + pom2].get_attribute("textContent"))


    for player in range(graczyB):
        pom2 = player*9
        numbersB[player] = (web_element[startB + pom2].get_attribute("textContent"))
        playersB[player] = (web_element[startB + 1 + pom2].get_attribute("textContent")).encode()
        posB[player] = (web_element[startB + 2 + pom2].get_attribute("textContent")).encode()
        teamB[player, 0] = (web_element[startB + 3 + pom2].get_attribute("textContent"))


    posA = np.char.decode(posA, encoding='ascii', errors='ignore')
    posB = np.char.decode(posB, encoding='ascii',  errors='ignore')
    playersA[graczyA] = " "
    playersB[graczyB] = " "
    posA[graczyA] = " "
    posB[graczyB] = " "
    numbersA[graczyA] = 0
    numbersB[graczyB] = 0
    
    playersA = np.char.decode(playersA, encoding=None, errors=None)
    playersB = np.char.decode(playersB, encoding=None, errors=None)
    playersA[graczyA] = "lacznie"
    playersB[graczyB] = "lacznie"


    #TEAM A
    #attack 126
    pom = 9*graczyA
    for player in range(graczyA):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 11] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamA[result, 10] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        teamA[result, 9] = (web_element[pom + 6 + pom2].get_attribute("textContent"))
        if(teamA[result, 9] == 0):   
            teamA[result, 12] = 0
            teamA[result, 13] = 0
        else:   
            teamA[result, 12] = "{:.2f}".format(float(teamA[result, 11]*100/teamA[result, 9]))
            teamA[result, 13] = "{:.2f}".format(float((teamA[result, 11]-teamA[result, 10])*100 / teamA[result, 9]))


    #block 238
    pom = 17*graczyA
    for player in range(graczyA):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 14] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamA[result, 15] = (web_element[pom + 5 + pom2].get_attribute("textContent"))


    #service 350
    pom = 25*graczyA
    for player in range(graczyA):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 4] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamA[result, 3] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        teamA[result, 2] = (web_element[pom + 6 + pom2].get_attribute("textContent"))
        if(teamA[result, 2] == 0):   
            teamA[result, 5] = 0
        else:  
            teamA[result, 5] = "{:.2f}".format(float((web_element[pom + 7 + pom2].get_attribute("textContent"))))


    #reception 462
    pom = 33*graczyA
    for player in range(graczyA):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA))[0])[0]

        teamA[result, 6] = (web_element[pom + 6 + pom2].get_attribute("textContent"))
        teamA[result, 7] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        if(teamA[result, 6] == 0):   
            teamA[result, 8] = 0
        else:  
            teamA[result, 8] = "{:.2f}".format(float(web_element[pom + 3 + pom2].get_attribute("textContent"))*100/teamA[result, 6])

        teamA[result, 1] = teamA[result, 0] - teamA[result, 3] - teamA[result, 7] - teamA[result, 10]


    #digs 574
    pom = 41*graczyA
    for player in range(graczyA):
        pom2 = player*7
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersA))[0])[0]

        teamA[result, 16] = (web_element[pom + 3 + pom2].get_attribute("textContent"))





    #TEAM B
    #attack
    pom = 9*graczyB + startB
    for player in range(graczyB):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 11] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamB[result, 10] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        teamB[result, 9] = (web_element[pom + 6 + pom2].get_attribute("textContent"))

        if(teamB[result, 9] == 0):   
            teamB[result, 12] = 0
            teamB[result, 13] = 0
        else:   
            teamB[result, 12] = "{:.2f}".format(float(teamB[result, 11]*100/teamB[result, 9]))
            teamB[result, 13] = "{:.2f}".format(float(teamB[result, 11]-teamB[result, 10])*100 / teamB[result, 9])


    #block
    pom = 17*graczyB + startB
    for player in range(graczyB):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 14] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamB[result, 15] = (web_element[pom + 5 + pom2].get_attribute("textContent"))


    #service
    pom = 25*graczyB + startB
    for player in range(graczyB):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 4] = (web_element[pom + 3 + pom2].get_attribute("textContent"))
        teamB[result, 3] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        teamB[result, 2] = (web_element[pom + 6 + pom2].get_attribute("textContent"))
        if(teamB[result, 2] == 0):   
            teamB[result, 5] = 0
        else:  
            teamB[result, 5] = "{:.2f}".format(float(web_element[pom + 7 + pom2].get_attribute("textContent")))


    #reception
    pom = 33*graczyB + startB
    for player in range(graczyB):
        pom2 = player*8
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 6] = (web_element[pom + 6 + pom2].get_attribute("textContent"))
        teamB[result, 7] = (web_element[pom + 4 + pom2].get_attribute("textContent"))
        if(teamB[result, 6] == 0):   
            teamB[result, 8] = 0
        else:  
            teamB[result, 8] = "{:.2f}".format(float(web_element[pom + 3 + pom2].get_attribute("textContent"))*100/teamB[result, 6])

        teamB[result, 1] = teamB[result, 0] - teamB[result, 3] - teamB[result, 7] - teamB[result, 10]


    #digs
    pom = 41*graczyB + startB
    for player in range(graczyB):
        pom2 = player*7
        result = ((np.where(float(web_element[pom + pom2].get_attribute("textContent")) == numbersB))[0])[0]

        teamB[result, 16] = (web_element[pom + 3 + pom2].get_attribute("textContent"))



    #team stats
    thislist = [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 14, 15, 16]

    przyjeciaA = 0
    przyjeciaB = 0

    for player in range(graczyA):
        for el in thislist:
            teamA[graczyA, el] = teamA[graczyA, el] + teamA[player, el]
        przyjeciaA = przyjeciaA + teamA[player, 6]*teamA[player, 8]/100

    for player in range(graczyB):
        for el in thislist:            
            teamB[graczyB, el] = teamB[graczyB, el] + teamB[player, el]
        przyjeciaB = przyjeciaB + teamB[player, 6]*teamB[player, 8]/100

        
    if(teamA[graczyA, 6] == 0):   teamA[graczyA, 8] = 0
    else:   teamA[graczyA, 8] = "{:.2f}".format(float(przyjeciaA*100/teamA[graczyA, 6]))

    if(teamB[graczyB, 6] == 0):   teamB[graczyB, 8] = 0
    else:   teamB[graczyB, 8] = "{:.2f}".format(float(przyjeciaB*100/teamB[graczyB, 6]))


    if(teamA[graczyA, 2] == 0):   teamA[graczyA, 5] = 0
    else:   teamA[graczyA, 5] = "{:.2f}".format(float((teamA[graczyA, 4] - teamA[graczyA, 3])*100 / teamA[graczyA, 2]))

    if(teamB[graczyB, 2] == 0):   teamB[graczyB, 5] = 0
    else:   teamB[graczyB, 5] = "{:.2f}".format(float((teamB[graczyB, 4] - teamB[graczyB, 3])*100 / teamB[graczyB, 2]))
    
    if(teamA[graczyA, 9] == 0):   teamA[graczyA, 12] = 0
    else:   teamA[graczyA, 12] = "{:.2f}".format(float(teamA[graczyA, 11]*100 / teamA[graczyA, 9]))

    if(teamB[graczyB, 9] == 0):   teamB[graczyB, 12] = 0
    else:   teamB[graczyB, 12] = "{:.2f}".format(float(teamB[graczyB, 11]*100 / teamB[graczyB, 9]))

    if(teamA[graczyA, 9] == 0):   teamA[graczyA, 13] = 0
    else:   teamA[graczyA, 13] = "{:.2f}".format(float((teamA[graczyA, 11] - teamA[graczyA, 10])*100 / teamA[graczyA, 9]))
    
    if(teamB[graczyB, 9] == 0):   teamB[graczyB, 13] = 0
    else:   teamB[graczyB, 13] = "{:.2f}".format(float((teamB[graczyB, 11] - teamB[graczyB, 10])*100 / teamB[graczyB, 9]))



    A = pd.DataFrame({'Nazwisko':playersA, 'Pozycja':posA, ' ':emptyA, 'Suma PKT':teamA[:,0].astype(int), 'Bilans':teamA[:,1].astype(int), ' ':emptyA, 'Zagrywki':teamA[:,2].astype(int),
        'Błędy':teamA[:,3].astype(int), 'Asy':teamA[:,4].astype(int), 'Eff %':teamA[:,5], ' ':emptyA, 'Przyjęcia':teamA[:,6].astype(int), 'Błędów':teamA[:,7].astype(int),
        'Perf%':teamA[:,8], ' ':emptyA, 'Ataki':teamA[:,9].astype(int), 'Bł/Bl':teamA[:,10].astype(int), 'Pkt':teamA[:,11].astype(int), 'Skut%':teamA[:,12],
        'Eff%':teamA[:,13], ' ':emptyA, 'Bloki':teamA[:,14].astype(int), 'Wybloki':teamA[:,15].astype(int), ' ':emptyA, 'Obrony':teamA[:,16].astype(int)},
        columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersA)

    B = pd.DataFrame({'Nazwisko':playersB, 'Pozycja':posB, ' ':emptyB, 'Suma PKT':teamB[:,0].astype(int), 'Bilans':teamB[:,1].astype(int), ' ':emptyB, 'Zagrywki':teamB[:,2].astype(int),
        'Błędy':teamB[:,3].astype(int), 'Asy':teamB[:,4].astype(int), 'Eff %':teamB[:,5], ' ':emptyB, 'Przyjęcia':teamB[:,6].astype(int), 'Błędów':teamB[:,7].astype(int),
        'Perf%':teamB[:,8], ' ':emptyB, 'Ataki':teamB[:,9].astype(int), 'Bł/Bl':teamB[:,10].astype(int), 'Pkt':teamB[:,11].astype(int), 'Skut%':teamB[:,12],
        'Eff%':teamB[:,13], ' ':emptyB, 'Bloki':teamB[:,14].astype(int), 'Wybloki':teamB[:,15].astype(int), ' ':emptyB, 'Obrony':teamB[:,16].astype(int)},
        columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersB)

    nameA = match + '_' + set + '_' + 'A.png'
    nameB = match + '_' + set + '_' + 'B.png'
    dfi.export(A, nameA)
    dfi.export(B, nameB)

    driver.close()

    return(name1, name2)


import tweepy
from credentials import * 
from datetime import datetime, timedelta
import pytz
import os

def on_tweet(tweet):
    words = (tweet.text).split()
    if(len(words)>2):
        username = tweet.author.screen_name
        nameA = words[1] + '_' + words[2] + '_' + 'A.png'
        #photo = open(nameA, 'rb')
        nameB = words[1] + '_' + words[2] + '_' + 'B.png'

        name1, name2 = fetch(words[1], words[2])


        filenames = [nameA, nameB]
        media_ids = []

        for filename in filenames:
            res = API.media_upload(filename)
            media_ids.append(res.media_id)

        if(words[2] == 'all'): words[2] = ', całość'
        else: words[2] = ', set ' + words[2] 
        comment = '@' + username + ' Mecz: ' + name1 + ' vs ' + name2 + words[2]

        API.update_status(status = comment, media_ids = media_ids, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
        
        os.remove(nameA)
        os.remove(nameB)


while(True):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    API = tweepy.API(auth)

    with open('time.txt') as f:
        text = f.readlines()
        date = datetime.strptime((str(text[0])[:19]), '%Y-%m-%d %H:%M:%S')
        date = pytz.utc.localize(date)

    with open('time.txt', 'w') as file:
        file.write(str(datetime.now()))

    tweets = tweepy.Cursor(API.search_tweets, q='@staty_kadra')
    if tweets is not None:
        for tweet in tweets.pages():
            for i in tweet:
                if (i.created_at + timedelta(hours=2) > date):
                    while 1:
                        try:
                            on_tweet(i)
                            break
                        except:
                            break
                        
    time.sleep(300)
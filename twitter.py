import string
from pyparsing import Char
from selenium import webdriver
from selenium.webdriver.common.by import By

import numpy as np
import pandas as pd
import dataframe_image as dfi

def fetch(match, set):
    link = "https://en.volleyballworld.com/volleyball/competitions/vnl-2022/schedule/" + match + "/#boxscore"

    query = "div[class='vbw-o-table-wrap'] table[class*='vbw-set-" + set + "'] td[class*='vbw-o-table__cell']"

    empty = np.empty((15), dtype=Char)

    for i in range(15):
        empty[i] = '|'

    numbersA = np.empty((15), dtype=int)
    numbersB = np.empty((15), dtype=int)

    posA = np.empty(15, dtype="S2")
    posB = np.empty(15, dtype="S2")

    playersA = np.empty(15, dtype="S18")
    playersB = np.empty(15, dtype="S18")

    teamA = np.zeros((15, 17))
    teamB = np.zeros((15, 17))

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe', options=op)

    driver.get(link)


    team = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-wrapper vbw-stats-by-player-wrapper'] div[class='vbw-mu__team__name']")

    name1 = team[0].get_attribute("textContent")
    name2 = team[1].get_attribute("textContent")


    web_element = driver.find_elements(By.CSS_SELECTOR, query)

    for player in range(14):
            numbersA[player] = (web_element[0 + player*9].get_attribute("textContent"))
            playersA[player] = (web_element[1 + player*9].get_attribute("textContent")).encode()
            posA[player] = (web_element[2 + player*9].get_attribute("textContent")).encode()
            teamA[player, 0] = (web_element[3 + player*9].get_attribute("textContent"))


    for player in range(14):
            numbersB[player] = (web_element[784 + player*9].get_attribute("textContent"))
            playersB[player] = (web_element[785 + player*9].get_attribute("textContent")).encode()
            posB[player] = (web_element[786 + player*9].get_attribute("textContent")).encode()
            teamB[player, 0] = (web_element[787 + player*9].get_attribute("textContent"))

    posA = np.char.decode(posA, encoding='ascii', errors='ignore')
    posB = np.char.decode(posB, encoding='ascii',  errors='ignore')
    playersA[14] = " "
    playersB[14] = " "
    posA[14] = " "
    posB[14] = " "
    numbersA[14] = 0
    numbersB[14] = 0
    playersA = np.char.decode(playersA, encoding=None, errors=None)
    playersB = np.char.decode(playersB, encoding=None, errors=None)
    playersA[14] = "lacznie"
    playersB[14] = "lacznie"


    #TEAM A
    #attack
    for player in range(14):
        result = ((np.where(float(web_element[126 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 11] = (web_element[129 + player*8].get_attribute("textContent"))
        teamA[result, 10] = (web_element[130 + player*8].get_attribute("textContent"))
        teamA[result, 9] = (web_element[132 + player*8].get_attribute("textContent"))
        if(teamA[result, 9] == 0):   
            teamA[result, 12] = 0
            teamA[result, 13] = 0
        else:   
            teamA[result, 12] = "{:.2f}".format(float(teamA[result, 11]*100/teamA[result, 9]))
            teamA[result, 13] = "{:.2f}".format(float((teamA[result, 11]-teamA[result, 10])*100 / teamA[result, 9]))


    #block
    for player in range(14):
        result = ((np.where(float(web_element[238 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 14] = (web_element[241 + player*8].get_attribute("textContent"))
        teamA[result, 15] = (web_element[243 + player*8].get_attribute("textContent"))


    #service
    for player in range(14):
        result = ((np.where(float(web_element[350 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
        
        teamA[result, 4] = (web_element[353 + player*8].get_attribute("textContent"))
        teamA[result, 3] = (web_element[354 + player*8].get_attribute("textContent"))
        teamA[result, 2] = (web_element[356 + player*8].get_attribute("textContent"))
        if(teamA[result, 2] == 0):   
            teamA[result, 5] = 0
        else:  
            teamA[result, 5] = "{:.2f}".format(float((web_element[357 + player*8].get_attribute("textContent"))))


    #reception
    for player in range(14):
        result = ((np.where(float(web_element[462 + player*8].get_attribute("textContent")) == numbersA))[0])[0]

        teamA[result, 6] = (web_element[468 + player*8].get_attribute("textContent"))
        teamA[result, 7] = (web_element[466 + player*8].get_attribute("textContent"))
        if(teamA[result, 6] == 0):   
            teamA[result, 8] = 0
        else:  
            teamA[result, 8] = "{:.2f}".format(float(web_element[465 + player*8].get_attribute("textContent"))*100/teamA[result, 6])

        teamA[result, 1] = teamA[result, 0] - teamA[result, 3] - teamA[result, 7] - teamA[result, 10]


    #digs
    for player in range(14):
        result = ((np.where(float(web_element[574 + player*7].get_attribute("textContent")) == numbersA))[0])[0]

        teamA[result, 16] = (web_element[577 + player*7].get_attribute("textContent"))






    #TEAM B
    #attack
    for player in range(14):
        result = ((np.where(float(web_element[910 + player*8].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 11] = (web_element[913 + player*8].get_attribute("textContent"))
        teamB[result, 10] = (web_element[914 + player*8].get_attribute("textContent"))
        teamB[result, 9] = (web_element[916 + player*8].get_attribute("textContent"))

        if(teamB[result, 9] == 0):   
            teamB[result, 12] = 0
            teamB[result, 13] = 0
        else:   
            teamB[result, 12] = "{:.2f}".format(float(teamB[result, 11]*100/teamB[result, 9]))
            teamB[result, 13] = "{:.2f}".format(float(teamB[result, 11]-teamB[result, 10])*100 / teamB[result, 9])


    #block
    for player in range(14):
        result = ((np.where(float(web_element[1022 + player*8].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 14] = (web_element[1025 + player*8].get_attribute("textContent"))
        teamB[result, 15] = (web_element[1027 + player*8].get_attribute("textContent"))


    #service
    for player in range(14):
        result = ((np.where(float(web_element[1134 + player*8].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 4] = (web_element[1137 + player*8].get_attribute("textContent"))
        teamB[result, 3] = (web_element[1138 + player*8].get_attribute("textContent"))
        teamB[result, 2] = (web_element[1140 + player*8].get_attribute("textContent"))
        if(teamB[result, 2] == 0):   
            teamB[result, 5] = 0
        else:  
            teamB[result, 5] = "{:.2f}".format(float(web_element[1141 + player*8].get_attribute("textContent")))


    #reception
    for player in range(14):
        result = ((np.where(float(web_element[1246 + player*8].get_attribute("textContent")) == numbersB))[0])[0]
        
        teamB[result, 6] = (web_element[1252 + player*8].get_attribute("textContent"))
        teamB[result, 7] = (web_element[1250 + player*8].get_attribute("textContent"))
        if(teamB[result, 6] == 0):   
            teamB[result, 8] = 0
        else:  
            teamB[result, 8] = "{:.2f}".format(float(web_element[1249 + player*8].get_attribute("textContent"))*100/teamB[result, 6])

        teamB[result, 1] = teamB[result, 0] - teamB[result, 3] - teamB[result, 7] - teamB[result, 10]


    #digs
    for player in range(14):
        result = ((np.where(float(web_element[1358 + player*7].get_attribute("textContent")) == numbersB))[0])[0]

        teamB[result, 16] = (web_element[1361 + player*7].get_attribute("textContent"))

    #team stats
    thislist = [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 14, 15, 16]

    przyjeciaA = 0
    przyjeciaB = 0

    for player in range(14):
        for el in thislist:
            teamA[14, el] = teamA[14, el] + teamA[player, el]
        przyjeciaA = przyjeciaA + teamA[player, 6]*teamA[player, 8]/100
        przyjeciaB = przyjeciaB + teamB[player, 6]*teamB[player, 8]/100
        
    if(teamA[14, 6] == 0):   teamA[14, 8] = 0
    else:   teamA[14, 8] = "{:.2f}".format(float(przyjeciaA*100/teamA[14, 6]))

    if(teamB[14, 6] == 0):   teamB[14, 8] = 0
    else:   teamB[14, 8] = "{:.2f}".format(float(przyjeciaB*100/teamB[14, 6]))


    if(teamA[14, 2] == 0):   teamA[14, 5] = 0
    else:   teamA[14, 5] = "{:.2f}".format(float((teamA[14, 4] - teamA[14, 3])*100 / teamA[14, 2]))

    if(teamB[14, 2] == 0):   teamB[14, 5] = 0
    else:   teamB[14, 5] = "{:.2f}".format(float((teamB[14, 4] - teamB[14, 3])*100 / teamB[14, 2]))
    
    if(teamA[14, 9] == 0):   teamA[14, 12] = 0
    else:   teamA[14, 12] = "{:.2f}".format(float(teamA[14, 11]*100 / teamA[14, 9]))

    if(teamB[14, 9] == 0):   teamB[14, 12] = 0
    else:   teamB[14, 12] = "{:.2f}".format(float(teamB[14, 11]*100 / teamB[14, 9]))

    if(teamA[14, 9] == 0):   teamA[14, 13] = 0
    else:   teamA[14, 13] = "{:.2f}".format(float((teamA[14, 11] - teamA[14, 10])*100 / teamA[14, 9]))
    
    if(teamB[14, 9] == 0):   teamB[14, 13] = 0
    else:   teamB[14, 13] = "{:.2f}".format(float((teamB[14, 11] - teamB[14, 10])*100 / teamB[14, 9]))



    A = pd.DataFrame({'Nazwisko':playersA, 'Pozycja':posA, ' ':empty, 'Suma PKT':teamA[:,0].astype(int), 'Bilans':teamA[:,1].astype(int), ' ':empty, 'Zagrywki':teamA[:,2].astype(int),
        'Błędy':teamA[:,3].astype(int), 'Asy':teamA[:,4].astype(int), 'Eff %':teamA[:,5], ' ':empty, 'Przyjęcia':teamA[:,6].astype(int), 'Błędów':teamA[:,7].astype(int),
        'Perf%':teamA[:,8], ' ':empty, 'Ataki':teamA[:,9].astype(int), 'Bł/Bl':teamA[:,10].astype(int), 'Pkt':teamA[:,11].astype(int), 'Skut%':teamA[:,12],
        'Eff%':teamA[:,13], ' ':empty, 'Bloki':teamA[:,14].astype(int), 'Wybloki':teamA[:,15].astype(int), ' ':empty, 'Obrony':teamA[:,16].astype(int)},
        columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersA)

    B = pd.DataFrame({'Nazwisko':playersB, 'Pozycja':posB, ' ':empty, 'Suma PKT':teamB[:,0].astype(int), 'Bilans':teamB[:,1].astype(int), ' ':empty, 'Zagrywki':teamB[:,2].astype(int),
        'Błędy':teamB[:,3].astype(int), 'Asy':teamB[:,4].astype(int), 'Eff %':teamB[:,5], ' ':empty, 'Przyjęcia':teamB[:,6].astype(int), 'Błędów':teamB[:,7].astype(int),
        'Perf%':teamB[:,8], ' ':empty, 'Ataki':teamB[:,9].astype(int), 'Bł/Bl':teamB[:,10].astype(int), 'Pkt':teamB[:,11].astype(int), 'Skut%':teamB[:,12],
        'Eff%':teamB[:,13], ' ':empty, 'Bloki':teamB[:,14].astype(int), 'Wybloki':teamB[:,15].astype(int), ' ':empty, 'Obrony':teamB[:,16].astype(int)},
        columns = ['Nazwisko','Pozycja', ' ', 'Suma PKT', 'Bilans', ' ', 'Zagrywki', 'Błędy', 'Asy', 'Eff %', ' ', 'Przyjęcia', 'Błędów', 'Perf%', ' ', 'Ataki', 'Bł/Bl', 'Pkt', 'Skut%', 'Eff%', ' ', 'Bloki', 'Wybloki', ' ', 'Obrony']).set_index(numbersA)

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
                on_tweet(i)
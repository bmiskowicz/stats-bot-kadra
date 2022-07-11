from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

import numpy as np

numbersA = np.empty((15), dtype=int)
numbersB = np.empty((15), dtype=int)

posA = np.empty(15, dtype="S2")
posB = np.empty(15, dtype="S2")

playersA = np.empty(15, dtype="S18")
playersB = np.empty(15, dtype="S18")

teamA = np.zeros((15, 17))
teamB = np.zeros((15, 17))

team1=[]
team2=[]

driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe')

driver.get("https://en.volleyballworld.com/volleyball/competitions/vnl-2022/schedule/13745/#boxscore")

WebDriverWait(driver, 5)

team = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-wrapper vbw-stats-by-player-wrapper'] div[class='vbw-mu__team__name']")

name1 = team[0].get_attribute("textContent")
name2 = team[1].get_attribute("textContent")

#print(name1 + " " + name2)

web_element = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-o-table-wrap'] table[class*='vbw-set-all'] td[class*='vbw-o-table__cell']")

#team1.append(web_element[126].get_attribute("textContent"))
#team1.append(web_element[238].get_attribute("textContent"))
#team1.append(web_element[350].get_attribute("textContent"))
#team1.append(web_element[462].get_attribute("textContent"))
#team1.append(web_element[574].get_attribute("textContent"))
#team1.append(web_element[672].get_attribute("textContent"))

team2.append(web_element[785].get_attribute("textContent"))
team2.append(web_element[787].get_attribute("textContent"))
team2.append(web_element[910].get_attribute("textContent"))
team2.append(web_element[1022].get_attribute("textContent"))
team2.append(web_element[1134].get_attribute("textContent"))
team2.append(web_element[1246].get_attribute("textContent"))
team2.append(web_element[1358].get_attribute("textContent"))
team2.append(web_element[1456].get_attribute("textContent"))

print(team1)
print(team2)
print(" ")

for player in range(14):
        numbersA[player] = (web_element[0 + player*9].get_attribute("textContent"))
        playersA[player] = (web_element[1 + player*9].get_attribute("textContent")).encode()
        posA[player] = (web_element[2 + player*9].get_attribute("textContent"))
        teamA[player, 0] = (web_element[3 + player*9].get_attribute("textContent"))


for player in range(14):
        numbersB[player] = (web_element[784 + player*9].get_attribute("textContent"))
        playersB[player] = (web_element[785 + player*9].get_attribute("textContent")).encode()
        posB[player] = (web_element[786 + player*9].get_attribute("textContent"))
        teamB[player, 0] = (web_element[787 + player*9].get_attribute("textContent"))

playersA = np.char.decode(playersA, encoding=None, errors=None)
playersB = np.char.decode(playersB, encoding=None, errors=None)
playersA[14] = "łącznie"
playersB[14] = "łącznie"
print(numbersA)
print(numbersB)
print(" ")
print(playersA)
print(playersB)
print(" ")
print(posA)
print(posB)
print(" ")



for player in range(14):
    result = ((np.where(float(web_element[126 + player*8].get_attribute("textContent")) == numbersA))[0])[0]
    
    teamA[result, 11] = (web_element[129 + player*8].get_attribute("textContent"))
    teamA[result, 10] = (web_element[130 + player*8].get_attribute("textContent"))
    teamA[result, 9] = (web_element[132 + player*8].get_attribute("textContent"))
    if(teamA[result, 9] == 0):   
        teamA[result, 12] = 0
        teamA[result, 13] = 0
    else:   
        teamA[result, 12] = teamA[result, 11]*100/teamA[result, 9]
        teamA[result, 13] = (teamA[result, 11]-teamA[result, 10])*100 / teamA[result, 9]




print(teamA)
#print(teamB)


driver.close()
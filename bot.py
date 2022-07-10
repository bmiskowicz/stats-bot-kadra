from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe')

driver.get("https://en.volleyballworld.com/volleyball/competitions/vnl-2022/schedule/13745/#boxscore")

team = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-wrapper vbw-stats-by-player-wrapper'] div[class='vbw-mu__team__name']")

team1 = team[0].get_attribute("textContent")
team2 = team[1].get_attribute("textContent")

#print(team1 + " " + team2)

web_element = driver.find_elements(By.CSS_SELECTOR, "div[class='vbw-o-table-wrap'] table[class*='vbw-set-all'] td[class*='vbw-o-table__cell']")

#print(len(web_element))

#for e in web_element:
#    print(e.get_attribute("textContent"))


driver.close()



from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import datetime

now = datetime.datetime.now()
driver = webdriver.Chrome('/Users/trevormcguire/PycharmProjects/NHLRankings/chromedriver')

currentranks = pd.read_csv('currentrankings.csv', index_col=0)

url = 'https://www.nhl.com/standings/2018/league'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

teams = soup.findAll('span', {'class': 'team--name'})

teamslist = []
ranklist = []
for i in range(31):
    team = str(teams[i])
    team = re.sub('<[^>]+>', '', team)
    teamslist.append(team)
    ranklist.append(str(i))

today = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
df = pd.DataFrame({today: teamslist, 'Rank': ranklist})
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]
df.to_csv('todayrankings.csv')

df2 = pd.concat([currentranks, df[df.columns[-1]]], axis=1)
df2.to_csv('currentrankings.csv')



import pandas as pd

ranks = open('currentrankings.csv', 'r+')
ranks = pd.read_csv(ranks)

ranks = ranks.replace('p-Tampa Bay', 'Tampa Bay')
ranks = ranks.replace('x-Tampa Bay', 'Tampa Bay')
ranks = ranks.replace('z-Calgary', 'Calgary')
ranks = ranks.replace('x-Calgary', 'Calgary')
ranks = ranks.replace('x-Boston', 'Boston')
ranks = ranks.replace('x-Washington', 'Washington')
ranks = ranks.replace('y-Washington', 'Washington')
ranks = ranks.replace('x-NY Islanders', 'NY Islanders')
ranks = ranks.replace('x-San Jose', 'San Jose')
ranks = ranks.replace('x-Pittsburgh', 'Pittsburgh')
ranks = ranks.replace('x-Winnipeg', 'Winnipeg')
ranks = ranks.replace('x-Nashville', 'Nashville')
ranks = ranks.replace('y-Nashville', 'Nashville')
ranks = ranks.replace('x-Carolina', 'Carolina')
ranks = ranks.replace('x-St. Louis', 'St. Louis')
ranks = ranks.replace('x-Vegas', 'Vegas')
ranks = ranks.replace('x-Dallas', 'Dallas')
ranks = ranks.replace('x-Columbus', 'Columbus')
ranks = ranks.replace('x-Colorado', 'Colorado')
ranks = ranks.replace('x-Toronto', 'Toronto')
ranks = ranks.replace('Washinton', 'Washington')
ranks = ranks.iloc[:,1:]


ranks.to_csv('cleanedrankings.csv', index=False)





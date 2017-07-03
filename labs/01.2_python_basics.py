#!usr/bin/python3

# For loops and list comprehensions
nums = range(1,6)

cubes = [num**3 for num in nums]

print(cubes) # [1, 8, 27, 64, 125]

letters = ['a', 'b', 'c']
letters_upper = [ letter.upper() for letter in letters]
print(letters_upper) # ['A', 'B', 'C']

word = 'abc'
word_upper = [letter.upper() for letter in word]
print(word_upper) # ['A', 'B', 'C']

# Dictionaries
fruits = {
    "apple": 2,
    "banana": 5,
    "kiwi": 4,
    "orange": 1
}

print(fruits['apple']) # 2
fruits['berries'] = 10
print(fruits)


# Requests 
import requests
r = requests.get('http://www.google.com')
type(r) # requests.models.Response
r.text

# csv 
import csv

# open csv from url
r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/2014-average-ticket-price.csv')
data_url = [row for row in csv.reader(r.iter_lines())]

# open a file for reading 
with open ('../data/2014-average-ticket-price.csv', 'rU') as f:
    data_file = [row for row in csv.reader(f)]

data = data_file[1:97]

# step 1: create a list that only contains events
events = [row[0] for row in data]

# step 2: create a list that only contains prices (stored as integers)
prices = [ int(row[2]) for row in data]

# Step 3: Calculate the overall average ticket price.
avg = sum(prices) // len(prices)
print(avg) # 35

# Step 4: Use a for loop to make a list of the away teams.
away_teams = []
for event in events: 
    stop_index = event.find(' at ')
    away_teams.append(event[:stop_index])
# print(away_teams)

# Step 5: Use a for loop to make a list of the home teams.
home_teams = []
for event in events:
    start_index = event.find(' at ') + 4
    stop_index = event.find(' Tickets ')
    home_teams.append(event[start_index:stop_index])
# print(home_teams)

# Step 6: Create a list of prices for Ravens home games
ravens_prices_home = [price for team, price in zip(home_teams, prices) if team == 'Baltimore Ravens']

# Step 7: Create a list of prices for Raves away games

ravens_prices_away = [price for team, price in zip(away_teams, prices) if team == 'Baltimore Ravens']
print(ravens_prices_away)

# Step 8: Calculate the average of each of the price lists
avg_ravens_price_home = float(sum(ravens_prices_home)) // len(ravens_prices_home)

avg_ravens_price_away = float(sum(ravens_prices_away)) // len(ravens_prices_away)

print(avg_ravens_price_home) # 157
print(avg_ravens_price_away) # 122


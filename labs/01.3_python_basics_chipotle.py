#!usr/bin/python3

'''
Chipotle data source: https://github.com/TheUpshot/chipotle
Article
'''

import csv 

'''
PART 1: Read in file with csv.reader() and store it in an object called 'file_nested_list'
'''
# open tsv file
with open('../data/chipotle.tsv', mode='r') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')]

'''
PART 2: Seperate into header and data
'''  
# first row is header 
header = file_nested_list[0]
# everything below header is data
data = file_nested_list[1:]

'''
PART 3: Calculate the average price of an order
'''
num_orders = len(set([row[0] for row in data]))
prices = [ float(row[4][1:-1]) for row in data]
# calculate avg; sum of prices / num of orders
avg_price_of_order = round(sum(prices) / num_orders, 2)


'''
PART 4: Create a list of all unique sodas 
''' 
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])

sodas = [ row[3][1:-1] for row in data if 'Canned' in row[2]]
unique_sodas = set(sodas)

'''
PART 5: Calculate average number of toppings per burrito.
'''
burritos = 0
toppings = 0
for row in data:
    if 'Burrito' in row[2]:
        burritos += 1
        toppings += (row[3].count(',') + 1)

avg_burrito_toppings = round(toppings / float(burritos), 2)
print(avg_burrito_toppings)


'''
PART 6: Create a dictionary in which the keys represent chip orders and the values represent total number of orders.
'''
chips = {}

for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = int(row[1])
        else:
            chips[row[2]] += int(row[1])

# defaultdict already checks if key is present or not
from collections import defaultdict
dchips = defaultdict(int)
for row in data:
    if 'Chips' in row[2]:
        dchips[row[2]] += int(row[1])

print(dchips)
#!usr/bin/python2

'''
Working with Chipotle data
'''

# path to data
data_path = '../data/chipotle.tsv'

import csv

# read tsv file using csv.reader, use delimiter \t for tab
with open(data_path, 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]


# separate header and data into different lists 
header = data[0]
data = data[1:]



'''
calculate avg price of an order
'''
# num of orders, use set data structure to filter repeats
num_orders = len(set([row[0] for row in data]))

# list of prices, use slicing or translate to remove $
prices = [ float(row[4].translate(None, '$'))for row in data] 

# avg price, round to 2 digits
round( sum(prices) / num_orders, 2) # $18.81



'''
create a unique list of all unique sodas and soft drinks
'''
sodas = [ row[3].translate(None, '[]') for row in data if 'Canned' in row[2]]
unique_sodas = set(sodas) # ['Sprite', 'Coke', 'Lemonade', 'Coca Cola', 'Diet Dr. Pepper', 'Diet Coke', 'Dr. Pepper', 'Nestea', 'Mountain Dew']


'''
create avg number of toppings per burrito
'''

burritos = len([row[2] for row in data if 'Burrito' in row[2]])

topppings = [(row[3].count(',') + 1) for row in data if 'Burrito' in row[2]]

round(sum(topppings) / float(burritos), 2) # 5.4 toppings per burrito


'''
create a dictionary in which key are chip orders and values are total number of orders 
'''

chips = list(set([ row[2] for row in data if 'Chips' in row[2] ]))

from collections import defaultdict
dchips = defaultdict(int)
for row in data:
    if row[2] in chips:
        dchips[row[2]] += int(row[1])


'''
create a dictionary in which key is the order id and value is the total price. Find the most expensive order
'''

dorders = defaultdict(int)
for row in data:
    dorders[row[0]] += float(row[4].translate(None, '$'))

max(dorders, key=dorders.get) # order 926: $205.25


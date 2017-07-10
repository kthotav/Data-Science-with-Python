#!usr/bin/python2
'''
File reading using Airline Safety Data
'''

data_path = '../data/airline-safety.csv'

# read the whole file at once, open file, read file, and close file
f = open(data_path, 'rU')
data = f.read()
f.close()


# alternative way to open, close file: use context manager to automatically close your file
with open(data_path, 'rU') as f:
    data = f.read()


# read the file into a list 
with open(data_path, 'rU') as f:
    data = []
    for row in f:
        data.append(row)


# read the file using list comprehension
with open(data_path, 'rU') as f:
    data = [row for row in f]


# split strings into a list
'Hello world! Good morning'.split() # ['Hello', 'world!', 'Good', 'morning']

# split with a delimter
'apple,banana,cherry'.split(',') # ['apple', 'banana', 'cherry']


# split each string into a list
with open(data_path, 'rU') as f:
    data = [row.split(',') for row in f]


# use csv module
import csv
with open(data_path, 'rU') as f:
    data = [row for row in csv.reader(f)]


# seperate header and data below header
header = data[0]
data = data[1:]


# a list containing the average number of incidents per year for each airline.
incidents = [round((int(row[2]) + int(row[5])) / float(30), 2) for row in data]


# a list of airline names (without the star)
# translate(None, '*') removes *
airlines = [row[0].translate(None, '*') for row in data]


# a list (of the same length) that contains 1 if there's a star and 0 if not
airlines_1 = [1 if '*' in row[0] else 0 for row in data]


# Create a dictionary in which the key is the airline name (without the star) and the value is the average number of incidents. 
airline_incidents = dict(zip(airlines, incidents))

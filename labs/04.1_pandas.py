#!usr/bin/python2

'''
MovieLens 100k movie rating data:
    main page: http://grouplens.org/datasets/movielens/
    data dictionary: http://files.grouplens.org/datasets/movielens/ml-100k-README.txt
    files: u.user, u.data, u.item
WHO alcohol consumption data:
    article: http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/    
    original data: https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption
    file: drinks.csv (with additional 'continent' column)
National UFO Reporting Center data:
    main page: http://www.nuforc.org/webreports.html
    file: ufo.csv
'''

import pandas as pd

# read text file
pd.read_table('../data/u.user')

# read u.user data into variable
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('../data/u.user', sep='|', header=None, names=user_cols, index_col = 'user_id', dtype={'age':int, 'zip_code':str})

type(users) # dataframe
users.head()   # print the first 5 rows
users.head(10) # print the first 10 rows
users.tail() # print the last 5 rows
users.index # index cols, user_id
users.columns # col names
users.dtypes # data types of each col
users.shape # number of rows and columns
users.values # prints data as NumPy array
users.info() # summarry of data

# select a column
users['gender']
type(users['gender']) # type series
users.gender # select one column using DataFrame object 

# summarize (describe) the data
users.describe() # describe all numeric columns, give count, mean, std, min, max
users.describe(include=['object']) # describe all object columns
users.describe(include='all') # describe all columns 
users.gender.describe() # describe single column
users.age.mean() # get mean of age column

# count number of occurrences of each value 
users.gender.value_counts() # useful for categorial variables M/F
users.age.value_counts() # useful for categorial numerical variables


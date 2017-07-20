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


'''
EXERCISE ONE
'''

# read drinks table 
drinks = pd.read_table('../data/drinks.csv', sep=',')
drinks = pd.read_csv('../data/drinks.csv')

# drinks head, tail data
drinks.head()
drinks.tail() 

# drinks data info
drinks.index
drinks.dtypes 
drinks.shape 

drinks['beer_servings']
drinks.beer_servings

# drinks data info with describe 
drinks.describe()
drinks.beer_servings.describe()
drinks.beer_servings.mean()

# count continent occurences
drinks.continent.value_counts()


'''
Filtering and Sorting
'''

# filter users less than 20 yrs of age
users[users.age < 20]
users[users.age < 20].occupation
users[users.age < 20].occupation.value_counts()

# filter with multiple condition 
users[(users.age < 20) & (users.gender == 'M')]
users[(users.age < 20) | (users.age > 60)]
users[users.occupation.isin(['doctor', 'lawyer'])] 

# sorting
users.age.sort_values () # sorts age column
users.sort_values(by='age') # sorts age column
users.sort_values(by='age', ascending=False) # use descending
users.sort_values(['occupation', 'age']) # sort by multiple columns



'''
EXERCISE TWO
'''

# filter DF to only include EU countries
drinks[drinks.continent == 'EU']

# filter DF to EU contries with wine servings > 30
drinks[(drinks.continent == 'EU') & (drinks.wine_servings > 300)]

# calcualte the average 'beer_servings for all EU
drinks[drinks.continent == 'EU'].beer_servings.mean()

# determine which 10 countries have highst total_liters_of_pure_alcohol
drinks.sort_values(by = 'total_litres_of_pure_alcohol').tail(10)

'''
Renaming, Adding, and Removing Columns 
'''

# renaming one or more columns 
drinks.rename(columns={'beer_servings': 'beer', 'wine_servings': 'wine'})
drinks.rename(columns={'beer_servings': 'beer', 'wine_servings': 'wine'}, inplace=True)

# replace all column names
drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv('../data/drinks.csv', header=0, names=drink_cols)
drinks.columns = drink_cols

# add a new column as a function of existing columns
drinks['servings'] = drinks.beer + drinks.spirit + drinks.wine
drinks['mL'] = drinks.liters * 1000

# removing columns
drinks.drop('mL', axis=1)
drinks.drop(['mL', 'servings'], axis=1)
drinks.drop(['mL', 'servings'], axis=1, inplace=True)   # make it permanent

'''
Handling Missing Values 
'''

drinks.continent.value_counts() # excludes missing values
drinks.continent.value_counts(dropna=False) # includes missing values

# finding missing values in a Series
drinks.continent.isnull() # True if missing, False if not missing
drinks.continent.isnull() # count the missing values
drinks.continent.notnull() # True if not missing, False if missing
drinks[drinks.continent.notnull()] # only shows rows where continent is not missing

# understandin axis
drinks.sum(axis = 0) # sums down the 0 axis, rows
drinks.sum() # axis is 0 by default 
drinks.sum(axis = 1) # sums across the 1 axis, columns

# find missing values in DF
drinks.isnull()
drinks.isnull().sum() # count missing values in each column

# drop missing values 
drinks.dropna() # drop a row if ANY values are missing
drinks.dropna(how="all") # drop only if ALL values are missing

# fill in missing values
drinks.continent.fillna(value='NA') # fill missing value with NA
drinks.continent.fillna(value='NA', inplace=True) # modifies 'drinks' in place

# turn of missing value filter 
drinks = pd.read_csv('../data/drinks.csv', header=0, names=drink_cols, na_filter=False)


'''
EXCERISE THREE
'''

# read ufo.csv
ufo = pd.read_csv('../data/ufo.csv')

# check shape of ufo data
ufo.shape

# most common colors 
ufo['Colors Reported'].value_counts()[:3]
ufo['Colors Reported'].value_counts().head(3)

# rename any columns with spaces so that they don't contain spaces
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
ufo.columns = [col.replace(' ', '_') for col in ufo.columns]

# find most common city of reports in VA
ufo[ufo.State == 'VA'].City.value_counts().head(1)

# print a DataFrame containing only reports from Arlington, VA
ufo[(ufo.City=='Arlington') & (ufo.State=='VA')]

# missing values in each column
ufo.isnull().sum()

# how many rows remain if we drop all rows with NaN
ufo.dropna().shape[0]
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

'''
Split-Apply-Combine
'''

# for each continent, calculate the mean beer servings
drinks.groupby('continent').beer.mean()

# for each continent, calculate the mean of all numeric columns
drinks.groupby('continent').mean()

# for each continent, describe beer servings
drinks.groupby('continent').beer.describe()

drinks.groupby('continent').beer.agg(['count', 'mean', 'min', 'max'])
drinks.groupby('continent').beer.agg(['count', 'mean', 'min', 'max']).sort_values(by='mean')

drinks.groupby('continent').describe()

# count number of occurrences of continent
drinks.groupby('continent').continent.count()
drinks.continent.value_counts()


'''
EXCERCISE FOUR
'''
# for each occupation in 'users', count the number of occurrences
users.occupation.value_counts()

# for each occupation, calculate the mean age
users.groupby('occupation').age.mean()

# for each occupation, calculate min and max age
users.groupby('occupation').age.agg(['min', 'max'])

# for each combination of occupation and gender, calculate the mean age
users.groupby(['occupation', 'gender']).age.mean()


'''
Selecting Multiple Columns and Flitering Rows
'''


# select multiple colunms 
my_cols = ['City', 'State']
ufo[my_cols]
ufo[['City', 'State']]

# use loc to select columns by name 
ufo.loc[:, 'City']
ufo.loc[:, ['City', 'State']]
ufo.loc[:, 'City':'State']

# loc can also filter rows
ufo.loc[0, :]
ufo.loc[0:2, :]
ufo.loc[0:2, 'City': 'State']

# use iloc to filter rows and select columns by integer position
ufo.iloc[:, [0,3]]
ufo.iloc[:, 0:4]
ufo.iloc[0:3, :]


'''
Merging DataFrames
'''

# read 'u.item' 
movie_cols = ['movie_id', 'title']
movies = pd.read_table('../data/u.item.txt', sep='|', header=None, names=movie_cols, usecols=[0,1])

# read u.data 
ratiing_cols = ['user.id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../data/u.data.txt', sep='\t', header=None, names=ratiing_cols )

# merge movies and ratings data (inner join)
movie_ratings = pd.merge(movies, ratings)
movies.shape
ratings.shape
movie_ratings.shape

'''
Other Commonly Used Features
'''

# map existing values to a different set of values
users['is_male'] = users.gender.map({'F':0, 'M':1})

# replace all instances of a value in a column (must match entire value)
ufo.State.replace('Fl', 'FL', inplace=True)

# string methods are accessed via 'str'
ufo.State.str.upper()                               # converts to uppercase
ufo.Colors_Reported.str.contains('RED', na='False') # checks for a substring

# convert a string to the datetime format
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.Time.dt.hour                        # datetime format exposes convenient attributes
(ufo.Time.max() - ufo.Time.min()).days  # also allows you to do datetime "math"

# setting and then removing an index
ufo.set_index('Time', inplace=True)
ufo.reset_index(inplace=True)

# change the data type of a column
drinks['beer'] = drinks.beer.astype('float')

# create dummy variables for 'continent' and exclude first dummy column
continent_dummies = pd.get_dummies(drinks.continent, prefix='cont').iloc[:, 1:]

# concatenate two DataFrames (axis=0 for rows, axis=1 for columns)
drinks = pd.concat([drinks, continent_dummies], axis=1)


'''
Other Less Used Features
'''

# detecting duplicate rows
users.duplicated()          # True if a row is identical to a previous row
users.duplicated().sum()    # count of duplicates
users[users.duplicated()]   # only show duplicates
users.drop_duplicates()     # drop duplicate rows
users.age.duplicated()      # check a single column for duplicates
users.duplicated(['age', 'gender', 'zip_code']).sum()   # specify columns for finding duplicates

# convert a range of values into descriptive groups
drinks['beer_level'] = 'low'    # initially set all values to 'low'
drinks.loc[drinks.beer.between(101, 200), 'beer_level'] = 'med'     # change 101-200 to 'med'
drinks.loc[drinks.beer.between(201, 400), 'beer_level'] = 'high'    # change 201-400 to 'high'

# display a cross-tabulation of two Series
pd.crosstab(drinks.continent, drinks.beer_level)

# convert 'beer_level' into the 'category' data type
drinks['beer_level'] = pd.Categorical(drinks.beer_level, categories=['low', 'med', 'high'])
drinks.sort('beer_level')   # sorts by the categorical ordering (low to high)

# limit which rows are read when reading in a file
pd.read_csv('drinks.csv', nrows=10)           # only read first 10 rows
pd.read_csv('drinks.csv', skiprows=[1, 2])    # skip the first two rows of data

# write a DataFrame out to a CSV
drinks.to_csv('drinks_updated.csv')                 # index is used as first column
drinks.to_csv('drinks_updated.csv', index=False)    # ignore index

# create a DataFrame from a dictionary
pd.DataFrame({'capital':['Montgomery', 'Juneau', 'Phoenix'], 'state':['AL', 'AK', 'AZ']})

# create a DataFrame from a list of lists
pd.DataFrame([['Montgomery', 'AL'], ['Juneau', 'AK'], ['Phoenix', 'AZ']], columns=['capital', 'state'])

# randomly sample a DataFrame
import numpy as np
mask = np.random.rand(len(drinks)) < 0.66   # create a Series of booleans
train = drinks[mask]                        # will contain around 66% of the rows
test = drinks[~mask]                        # will contain the remaining rows

# change the maximum number of rows and columns printed ('None' means unlimited)
pd.set_option('max_rows', None)     # default is 60 rows
pd.set_option('max_columns', None)  # default is 20 columns
print drinks

# reset options to defaults
pd.reset_option('max_rows')
pd.reset_option('max_columns')

# change the options temporarily (settings are restored when you exit the 'with' block)
with pd.option_context('max_rows', None, 'max_columns', None):
    print drinks
## 2. Sets ##

gender = []
for legislator in legislators:
    gender.append(legislator[3])
gender = set(gender)    
print(gender)

## 3. Exploring the Dataset ##

party = []
for legislator in legislators:
    party.append(legislator[6])
    
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##


for legislator in legislators:
    if legislator[3] == "":
        legislator[3] = "M"

## 5. Parsing Birth Years ##

birth_years = []
for legislator in legislators:
   
    parts = legislator[2].split('-')
    
    birth_years.append(parts[0])
    
    

## 6. Try/except Blocks ##

try:
    float('hello')
except:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for birth_year in birth_years:
    year = birth_year
    try:
        year = int(year)
    except Exception:
        pass
    
    converted_years.append(year)
    

## 9. Convert Birth Years to Integers ##

for legislator in legislators:
    
    parts = legislator[2].split('-')
    birth_year = parts[0]
    
    # convert year to int
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
        
    legislator.append(birth_year)
    
    
    

## 10. Fill in Years Without a Value ##

last_value = 1
for legislator in legislators:
    
    if legislator[7] == 0:
        legislator[7] = last_value
    
    last_value = legislator[7]
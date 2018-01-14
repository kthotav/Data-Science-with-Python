## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    
    print(ships[i])
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]


for i, thing in enumerate(things):
    
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [apple_price*2 for apple_price in apple_prices]
apple_prices_lowered = [apple_price-100 for apple_price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for legislator in legislators:
    
    if legislator[3] == 'F' and legislator[7] > 1940:
        
        name = legislator[1]
        
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1
            
    

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for value in values:
    if value is not None and value > 30:
        checks.append(True)
    else:
        checks.append(False)
        

## 8. Highest Female Name Count ##

max_value = None

for key in name_counts:
    count = name_counts[key]
    if max_value is None or count > max_value:
        max_value = count
    
    
    
    

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for plant, plant_type in plant_types.items():
    print(plant)
    print(plant_type)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for name, count in name_counts.items():
    
    if count == 2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = dict()

for legislator in legislators:
    
    
    if legislator[3] == 'M' and legislator[7] > 1940:
        
        if legislator[1] in male_name_counts:
            male_name_counts[legislator[1]] =  male_name_counts[legislator[1]]  + 1
        else:
             male_name_counts[legislator[1]] = 1
                
highest_male_count = None                
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count 
    

for name, count in male_name_counts.items():
    
    if count == highest_male_count:
        top_male_names.append(name)

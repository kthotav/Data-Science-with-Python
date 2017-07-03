#!/usr/bin/python3

def main():
    # Basic Data Types
    x = 5
    print (type(x)) # int
    print (type(5)) # int

    print(type(5.0)) # float
    print(type('five')) # str
    print(type(True)) # bool

    # Lists
    nums = [1, 2, 3.0, 'four'] # multiple data types
    print(nums)
    print(type(nums)) # list
    nums.append(5)
    nums.remove('four')
    print(nums)

    # List slicing [start:end:step]
    weekdays = ['mon','tues','wed','thurs','fri']
    weekdays[0]         # element 0
    weekdays[0:3]       # elements 0, 1, 2
    weekdays[:3]        # elements 0, 1, 2
    weekdays[3:]        # elements 3, 4
    weekdays[-1]        # last element (element 4)
    weekdays[::2]       # every 2nd element (0, 2, 4)
    weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

    days = weekdays + ['sat', 'sun'] # concat lists

    # Functions 
    def five():
        return 5

    print(five())

    def calc(x, y, op):
        if op == 'add':
            return x + y
        elif op == 'sub':
            return x - y
        else:
            print('Only add and sub allowed')

    print(calc(5, 3, 'add'))
    print(calc(5, 3, 'sub'))
    print(calc(5, 3, 'divide'))


    # For loops
    for i in range(5):
        print(i)

    fruits = ['apple', 'banana', 'cherry']
    for i,fruit in enumerate(fruits):
        print(i, fruit)

    for fruit in fruits:
        print(fruit.upper())
    
    fizz_buzz()

# Fizzbuzz
def fizz_buzz():
    nums = range(1,101)
    for num in nums:
        if num % 15 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)
        


if __name__ == "__main__": main()
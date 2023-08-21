#List Comprehension
'''
Exercise 1
'''
'''
It that takes a list of numbers and returns a list of the squares of the numbers.
'''
numbers = [9,10,11,12,14,15,16]
squared_numbers = [num**2 for num in numbers] 
'''instead of appending to a new list.'''
print(f'list of squared_numbers is {squared_numbers}')
# Expected output: [81, 100, 121, 144, 196, 225, 256]


'''
Exercise 2
filter the list to exclude negative numbers'''
list = [5,7,-13,6,0,12,-1]
list = [x for x in list if x > 0]
print(f'list with positive numbers only is {list}')
    # Expected output:[5, 7, 6, 12]
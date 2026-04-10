#METHOD1 using for loop
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []   # empty list to store unique elements

for num in numbers:   # loop through each element
    if num not in unique:   # check if already present
        unique.append(num)  # if not, add it

print(unique)

#Method 2 using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)  # automatically removes duplicates
print(list(unique))  # convert back to list and print

#Method 3 using ORDER + FAST – BEST METHOD
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(numbers))  # preserves order and removes duplicates
print(unique)

#METHOD 4 (SET + LOOP – Controlled)
numbers = [1, 2, 2, 3, 4, 4, 5]

seen = set() # to keep track of seen numbers
unique = []

for num in numbers:
    if num not in seen:
        seen.add(num) # add to seen set
        unique.append(num) # add to unique list only if it's not seen before

print(unique)

#METHOD 5 (LIST COMPREHENSION + SET)
numbers = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = [num for num in numbers if not (num in seen or seen.add(num))] # list comprehension to create unique list while adding to seen set
print(unique)



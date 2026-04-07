#METHOD 1--Loop v important
numbers=[9,5,6,3,7,88,98,90,23,45]

largest_num=numbers[0]  # assume first number is largest
smallest_num=numbers[0] # assume first number is smallest

for num in numbers:
    if num >largest_num: # compare current number with largest number
        largest_num=num  # update largest number
        print("largest number is:",largest_num) # print statement inside the loop to see how largest number is updated
        
    if num<smallest_num: # compare current number with smallest number
        smallest_num=num  # update smallest number
        print("smallest number is:",smallest_num) # print statement inside the loop to see how smallest number is updated

print("Largest number is:",largest_num)
print("Smallest number is:",smallest_num)

##Method 2--Built in functions
numbers=[9,5,6,3,7,88,98,90,23,45]

largest_num=max(numbers) # max function to find largest number
smallest_num=min(numbers) # min function to find smallest number

print("The largest number is:" , largest_num)
print("The smallest number is:" , smallest_num)

##METHOD 3--Sorting
numbers=[9,5,6,3,7,88,98,90,23,45]
numbers.sort() # sort the list in ascending order
print("Sorted numbers:",numbers) # print the sorted list to see the order

smallest_num=numbers[0] # first element is the smallest
largest_num=numbers[-1] # last element is the largest

print("The largest number is:" , largest_num)
print("The smallest number is:" , smallest_num)

##METHOD 4--(ADVANCED – USING INFINITY)

numbers=[9,5,6,3,7,88,98,90,23,45]

largest_num=float('-inf') # initialize largest number to negative infinity because any number will be larger than negative infinity
smallest_num=float('inf') # initialize smallest number to positive infinity because any number will be smaller than positive infinity

for num in numbers:
    if num >largest_num: # compare current number with largest number
        largest_num=num  # update largest number
        
    if num<smallest_num: # compare current number with smallest number
        smallest_num=num  # update smallest number

print("So the largest number is:" , largest_num)
print("So the smallest number is:" , smallest_num)
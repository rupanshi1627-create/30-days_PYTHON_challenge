#Method 1 --loop
numbers = [10, 5, 20, 7, 8]
largest=float('-inf') #initialize largest to negative infinity
second_largest=float('-inf') #initialize second largest to negative infinity

for num in numbers:
    if num>largest: #if current number is greater than largest
        second_largest=largest #update second largest to previous largest
        largest=num #update largest to current number
        
    elif num>second_largest and num!=largest: #if current number is greater than second largest and not equal to largest
        second_largest=num #update second largest to current number
print("The second largest number is:", second_largest) 

#METHOD 2 --SORTING
numbers = [10, 5, 20, 7, 8]
numbers.sort() #sort the list in ascending order
print(numbers) #print the sorted list
second_largest=numbers[-2] #the second largest number will be the second last element in the sorted list
print("The second largest number is:", second_largest)

#METHOD 3 --SET + SORTING
nums = [15, 5, 20, 20, 8]

nums = list(set(nums))   # duplicates remove
nums.sort()

print(nums[-2])

#OR
nums = [10, 5, 20, 8]

print(sorted(set(nums))[-2])
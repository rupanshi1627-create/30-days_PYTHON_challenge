#--METHOD1

numbers=[1,5,6,7,8]

Total=0 #assume in starting the sum is 0

for number in numbers:
    Total=number+Total
    print("The total sum is:" , Total)
 
print(Total)
 
 #METHOD 2--Built in function
numbers=[1,5,6,7,8]
Total=sum(numbers) #sum function to find the total sum of the list
print("The total sum is:" , Total)

#METHOD 3--Using while loop
numbers=[1,5,6,7,8]

Total=0 #assume in starting the sum is 0
i=0 #initialize index to 0 here using i because we are using while loop and we need to access the elements of the list using index

while i < len(numbers): #mean while loop will run until the index is less than the length of the list
    Total=Total+numbers[i]
    i+=1 #update the index by 1 to move to the next element in the list, we use i+=1 because we are using while loop and we need to update the index manually.
print("So the  total sum is:" , Total)


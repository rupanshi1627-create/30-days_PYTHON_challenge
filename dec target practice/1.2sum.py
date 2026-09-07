nums=[1,2,3,4,5,6,7,,8,9,10]
target=10
#we have to find the pairs whose sum is 10 

left=0 #we will start from left and consider that its the first nummber we are taking
right=len(nums)-1

while left<right:
    current_sum=num[left]+num[right]
    if current_sum==target:
        print(num[left],num[right])
    elif left<right:
        left+=1
    else:
        right-=1

#loop se bhaar
else:
print("no pair found")
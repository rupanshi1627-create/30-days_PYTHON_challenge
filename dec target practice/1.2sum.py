# Test 1:
nums = [2, 7, 11, 15]
target = 9
# Expected: [0, 1]
left=0
right=len(nums)-1

while left<right:
    current_sum=nums[left]+nums[right]
    if current_sum==target:
        print(left,right)
    elif current_sum<target:
        left+=1
    else:
        right-=1


print(current_sum)




# Test 2:
nums = [1, 3, 4, 5, 7, 11]
target = 9
# Test 1:
nums = [2, 7, 11, 15]
target = 9
# Expected: [0, 1]
left=0
right=len(nums)-1

while left<right:
    current_sum=nums[left]+nums[right]
    if current_sum==target:
        print(left,right)
    elif current_sum<target:
        left+=1
    else:
        right-=1
print(current_sum)

# Test 3:
nums = [1, 2, 3, 4, 5]
target = 9
# Expected: [3, 4] (because nums[3]=4, nums[4]=5, and 4+5=9)
# Test 1:
nums = [2, 7, 11, 15]
target = 9
# Expected: [0, 1]
left=0
right=len(nums)-1

while left<right:
    current_sum=nums[left]+nums[right]
    if current_sum==target:
        print(left,right)
    elif current_sum<target:
        left+=1
    else:
        right-=1

print(current_sum)
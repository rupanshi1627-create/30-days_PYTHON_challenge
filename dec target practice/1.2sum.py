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
# Expected: [2, 4] (because nums[2]=4, nums[4]=7, and 4+7=11... wait that's 11)
# Actually: [1, 3] (because nums[1]=3, nums[3]=5, and 3+5=8... no)
# Let me think... [0, 4] (because nums[0]=1, nums[4]=7, and 1+7=8... no)
# [3, 5] (because nums[3]=5, nums[5]=11... 5+11=16, no)
# Actually target 9: [2, 3] (4+5=9) ✓

# Test 3:
nums = [1, 2, 3, 4, 5]
target = 9
# Expected: [3, 4] (because nums[3]=4, nums[4]=5, and 4+5=9)
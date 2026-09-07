# Test 1:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
nums=[1,2,3,4,5,6,7,8,9,10]
target=10
left=0
right=len(nums)-1
#create a empty list to stpre pairs
pairs=[] # Changed 'pair' to 'pairs' to match usage

while left<right:
  current_sum=nums[left]+nums[right]
  if current_sum==target:
    pairs.append((nums[left],nums[right]))
    left+=1
    right-=1
  elif current_sum<target: # Corrected indentation
    left+=1
  else: # Corrected indentation
    right-=1
if pairs:
  for pair in pairs:
    print(pair[0],pair[1])
else:
  print("no pairs found")
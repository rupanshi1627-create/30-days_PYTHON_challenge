#TWO SUM 
# Test 1:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        print(nums[left], nums[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
else:
    print("No two numbers found that add up to the target.")
#container with max water when an array of heights is given 

height = [1,8,6,2,5,4,8,3,7]
target=49
left=0
right=len(height)-1

#max_water

while left<right:
    width=left-right
    height=min(height[left],height[right])
    current_water=width*height
    target=max(target,current_water)
    
    if height[left]<height[right]:
        left+1
    else:
        right-=1

print(target)
    
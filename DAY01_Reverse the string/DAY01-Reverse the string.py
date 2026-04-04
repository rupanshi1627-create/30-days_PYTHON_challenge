#1 WAY--slicing--REVERSE THE STRING
name="Roops"
reverse=""
i=len(name)-1     #length hai 3 so we aree starting from last index 4-1 
while i >= 0:     #Jab tak index valid hai (0 ya usse bada), tab tak loop chalega
    reverse=reverse + name[i]
    i-=1
    print(reverse)
print(reverse)

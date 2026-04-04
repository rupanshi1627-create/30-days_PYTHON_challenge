#PALINDROME--Numbers which are same from both the side--MADAM,LEVEL,NITIN
#3 ways--Slicing,logic,loop

#1---SLICING
Name="MADAMs"
reverse=Name[::-1]
if Name==reverse:
    print("This is palindrome")
else:
    print("This is not a palindrome")

#2---Loop

String="SHIHS"
reverse=''
for char in String:
    reverse=char + reverse
print(reverse)
if String==reverse:
    print("This is palindrome")
else:
    print("This is not a palindrome")
    
#3---LOGIC--interview king
#while loop and ek character i start se lenge and ek character j end se lenge sort

s="BOSSES"

i=0
j=len(s)-1

while i<j:  #ja tak j peeche se i ko cross nahi kar pata and i j se chhota hai
    if s[i]==s[j]:
        i+=1 ## agar same hai → i ko aage badhao (next character check karne ke liye)
        j-=1 # j ko peeche lao (last se next character check karne ke liye)
    else:
        print("This is not a palindrome")  # turant bol do → palindrome nahi hai
    break  
        # loop yahin rok do (aage check karne ki zarurat nahi)   
else:
    print("Palidrome")    
# ye else WHILE loop ke saath hai (important)
# ye tab chalega jab loop normally complete ho jaye (break na lage)
 


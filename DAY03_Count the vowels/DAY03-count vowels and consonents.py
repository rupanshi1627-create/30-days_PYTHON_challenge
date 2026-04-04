#DAY 03 COUNT VOWELS AND CONSONENTS
#VOWELS--a,e,i,o,u and rest are consonents
#How to count vowels?-----------
#Loop + condition
#Using isalpha() ----isalpha is a built in fucntion in python whhich checks whether this given is alphabet or not 
#Pythonic sum() approach
#----VV IMP thing that python is case senstive "A" ≠ "a" so we use ch.lower()--which makes each thing in lower case
print("A".lower())   # a
print("R".lower())   # r

name=input("Enter your string : ")
vowels=0
consonents=0

for ch in name:
    if ch.lower() in "aieou":  # agar char lower case me a,e,i,o,u me se kisi ke barabar hai to
        vowels+=1  # vowels ko 1 se badhao
    elif ch.lower() >='a'and ch.lower() <='z':  # agar char lower case me a se z ke beech me hai to
        consonents+=1  # consonents ko 1 se badhao
print("Vowels:",vowels)
print("Consonents:",consonents)

##-------------------2ND WAY USING ch.inalpha()-----------------
name=input("Pls enter any sentence here:")
vowels=0
consonents=0

for ch in name:
    if ch.isalpha():
        if ch.lower() in "aieou":
            vowels+=1
    else:
        consonents+=1
print("vowel: ", vowels)
print("consonent:", consonents)
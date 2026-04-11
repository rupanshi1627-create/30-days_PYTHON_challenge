#METHOD 1 --loop
#Prime number = jo sirf 1 aur khud se divide hota hai
#If a number from 2 to -num if divisible by any number then it is not a prime number    

numbers = [2,1,5,7, 4, 6, 8, 9, 13, 12, 16]

for num in numbers:
    if num <= 1:
        print(num, "is Not Prime")  #0, 1 are not prime numbers
        continue
    for i in range(2,num):
        if num%i==0: #if num is divisible by i then it is not a prime number
            print(num, "is Not Prime")
            break
    else:
        print(num, "is Prime")
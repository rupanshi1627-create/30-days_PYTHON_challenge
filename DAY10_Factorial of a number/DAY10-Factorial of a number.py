## Factorial means the product of all the integers from 1 to n. For example,
# the factorial of 5 is 120 (1*2*3*4*5). The factorial of 0 is defined to be 1.

n=10
factorial=1 # initialize factorial to 1
for i in range(1, n+1): # loop from 1 to n (inclusive)
    factorial=factorial*i # multiply current value of factorial with i
    print(factorial) # print the current value of factorial
    
print(factorial) # print the final value of factorial after the loop ends
    
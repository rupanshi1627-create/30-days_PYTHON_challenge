#Fibonacci Series
#next number = previous 2 numbers sum
#METHOD 1 --LOOP
def fibonacci(n):
    a = 0         # first number
    b = 1        # second number

    for i in range(n):   # loop n times

        print(a, end=" ")   # print current number

        c = a + b       # next number = sum of previous two
        a = b           # shift: a becomes old b
        b = c           # shift: b becomes new number


# function call
fibonacci(10)
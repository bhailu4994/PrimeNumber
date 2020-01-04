# That is a simple function to show if a number is prime or not
# The prime number must be divisible by itself and 1 only.

while True:
    n = int(input('Enter a number to see if it is prime or not:\n'))
    if n == 2:
        print('The number is prime')
    elif n > 2:
        for x in range(2,n):
            if n%x == 0:
                print('The number is not prime')
                break
        else:
            print('The number is prime')
    else:
        print('The number is not prime')
    break    

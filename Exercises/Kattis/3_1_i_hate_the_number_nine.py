#for T test cases, each consisting of an integer D, how many numbers are there of D digits that DO NOT contain any 9's?
#sounds weird at first, but I think it's super simple; the difficulty of this primarily comes from the problem of efficiency, in that you have to compute results with large values for D in under 1 second.

#the first digit can have value 1-8, any digit after can have value 0-8
#from that we get a simple formula
##because of high output values, the question specifies mod 1,000,000,007

# output = (8*(9**(digits-1)))%1000000007

#the above is our formula, but it's too inefficient for high numbers of digits; let's break it down to a custom function, which is a common efficient power function for python, but with our base-result set to 8 to match our formula.
def custom_power(x, y, p): 
    res = 8     # Initialize result 
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
    while (y > 0) :        
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p         
    return res
    
#first input: num test cases
num_cases = int(input())

#for each test case, get the num digits
for _ in range(num_cases):
    digits = int(input())

    output = custom_power(9,digits-1,1000000007)

    print(output)
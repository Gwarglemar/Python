#https://open.kattis.com/problems/data

#first input 1<=N<=14 ; denotes number of integers to follow
#second input: N integers from above, where each of X <= 1000, all positive
#give N values for X, Output = S where S is# of distinct prime factors in sum of all X

import math 
  
# A function to get a list of all prime factors of a given number n 
def primeFactors(n): 
    while n % 2 == 0: 
        print(2), 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            print(i), 
            n = n / i 
    if n > 2: 
        print(n)
    else:
        print(0)
  
test = [4,7,8]
sums = []

primeFactors(n) 
  
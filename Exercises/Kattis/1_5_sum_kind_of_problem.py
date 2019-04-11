#For this problem you will compute various running sums of values for positive integers.

#this one took me a bit to figure out; I got a working solution, but it was inefficient and Kattis requires your solutions be under a certain amount of required CPU time. I eventually looked up a formula for these instead of creating ranges to compute sums.

# import time

#get number of inputs:
num_inputs = int(input())
inputs = []

#Get the input data
index = 0
for _ in range(num_inputs):
    inputs = input().split()
    
    # t0 = time.time()
    
    n = int(inputs[1])
    
    # The sum of the first N positive integers.
    s1 = sum(range(1,n+1))

    # t1 = time.time()
    
    # The sum of the first N odd integers.
    s2 = ((2*n)*(n/2))

    # s3 = 0
    # nums=0
    # x=1
    # while nums < n:
    #     s2 += x
    #     nums += 1
    #     x += 2

    # t2 = time.time()

    # The sum of the first N positive integers.
    s3 = ((2*n+2)*(n/2))

    # s3 = 0
    # nums=0
    # x=2
    # while nums < n:
    #     s3 += x
    #     nums+=1
    #     x += 2

    # t3 = time.time()
    
    #output
    print('{0} {1} {2} {3}'.format(inputs[0],int(s1),int(s2),int(s3)))

    # testing/debugging
    # print('t1: ' + str(t1-t0))
    # print('t2: ' + str(t2-t1))
    # print('t3: ' + str(t3-t2))
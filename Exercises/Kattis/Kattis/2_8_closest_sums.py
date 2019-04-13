# Given is a set of integers and then a sequence of queries. A query gives you a number and asks to find a sum of two distinct numbers from the set which is closest to the query number.

# import time
# import random

case_num = 1
num_runs = 3

#FOR TESTING
# time_sum = 0

# while True:
while case_num <= num_runs:
    
    # t0 = time.time()

    #first input is int specifying number of values in dataset, followed by those values
    ns = []
    num_n = int(input())
    for _ in range(num_n):
        ns.append(int(input()))
    #second input is int specifying number of queries in the case, followed by those integers to query
    qs = []
    num_q = int(input())
    for _ in range(num_q):
        qs.append(int(input()))

    # for testing, build the inputs:
    # num_n = 1000
    # low_bound = -10**6
    # ns = [random.randint(low_bound,abs(low_bound)) for _ in range(num_n)]
    # num_q = 24
    # qs = [random.randint(low_bound,abs(low_bound)) for _ in range(num_q)]
    # num_n = 5
    # ns = [3,12,17,33,34]
    # num_q = 3
    # qs = [1,51,30]

    print(f"Case {case_num}:")

    # t1 = time.time()
    # print("Get inputs: " + str(t1-t0))

    ###GET SUMS

    #brute force method: create a Set of possible sums, then compare the queries to that.
    sums = []
    for x in range(len(ns)):
        for y in range(x+1,len(ns)):
            if x!=y:
                sums.append(ns[x]+ns[y])
    sums = list(set(sums))

    # t2 = time.time()
    # print("Get sums: " + str(t2-t1))

    ###RUN QUERIES

    for q in qs:
        closest = sums[0]
        best_diff = abs(q-closest)
        for s in sums:
            if abs(q-s) < best_diff:
                closest = s
                best_diff = abs(q-s)

        print(f"Closest sum to {q} is {closest}.")
  
    # t3 = time.time()
    # time_sum += (t3-t2)
    # print("Run queries: " + str(t3-t2))  

    case_num += 1

#TESTING
# print("Average Run-time: " + str(time_sum/num_runs)) 
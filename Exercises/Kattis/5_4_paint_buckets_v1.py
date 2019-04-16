#https://open.kattis.com/problems/paintbuckets

# from bisect import bisect_left

import time
import random

#first input: number of buckets and number of orders
# x = input().split()
# num_b = int(x[0])
# num_o = int(x[1])

# buckets = []
# orders = []
# for _ in range(num_b):
#     buckets.append(input())
# for _ in range(num_o):
#     orders.append(input())

### TEST DATA - accuracy
# num_b = 9
# num_o = 6

# buckets = ['5000000 100','5001000 100','5002000 100','6000000 100','6001000 100','6002001 100','7000000 100','7001001 100','7002001 100']
# orders = ['5001000 301','5001000 300','6001000 201','6001000 200','7001001 201','7001001 200']
### TEST DATA - efficiency
num_b = 200000
num_o = 100

def gen_item():
    x = str(random.randint(1,10**9))
    y = str(random.randint(1,10**4))
    return str(x) + ' ' + str(y)

buckets = [gen_item() for _ in range(num_b)]
orders = [gen_item() for _ in range(num_o)]
### END TEST DATA

t0 = time.time()

#Convert buckets to tuples of ranges
for i in range(len(buckets)):
    buckets[i] = buckets[i].split()
    buckets[i] = [int(buckets[i][0])-1000,int(buckets[i][0])+1000,int(buckets[i][1])]

for i in range(len(orders)):
    orders[i] = list(map(int,orders[i].split()))

t1 = time.time()
print('convert lists: ' + str(t1-t0))

# ts1 = time.time()
# buckets = sorted(buckets,key=lambda x:x[0])
# orders = sorted(orders,key=lambda x:x[0])

# ts2 = time.time()
# print('sort lists: ' + str(ts2-ts1))

#Orders Loop
for o in orders:
    ### FIRST TRY: nested For loops
    # bucket for loop
    t3 = time.time()
    for b in buckets:
        #if in range, subtract bucket qty from order qty
        if o[0] >= b[0] and o[0] <= b[1]:
            o[1] -= b[2]
            if o[1] <= 0:
                break
    t4 = time.time()
    print('bucket loop: ' + str(t4-t3))

    t4 = time.time()
    print("search time: " + str(t4-t3))
    
    #if order qty > 0 : fail : else : success
    if o[1] > 0:
        print('no')
    else:
        print('yes')

tx = time.time()
print('Full orders loop: ' + str(tx-t1))

# print('\n\n')
# print(orders)

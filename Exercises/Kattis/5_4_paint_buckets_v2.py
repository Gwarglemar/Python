#https://open.kattis.com/problems/paintbuckets

from bisect import bisect_left

# import time
# import random

# t0 = time.time()

#binary search function: find leftmost index of value >= X
def binary_left(search_list,search_val):
    i = bisect_left(search_list,search_val)
    if i != len(search_list):
        return i
    raise ValueError

#first input: number of buckets and number of orders
x = input().split()
num_b = int(x[0])
num_o = int(x[1])

buckets = []
orders = []
for _ in range(num_b):
    buckets.append(input())
# for _ in range(num_o):
#     orders.append(input())

### TEST DATA - accuracy
# num_b = 9
# num_o = 6

# buckets = ['5000000 100','5001000 100','5002000 100','6000000 100','6001000 100','6002001 100','7000000 100','7001001 100','7002001 100']
# orders = ['5001000 301','5001000 300','6001000 201','6001000 200','7001001 201','7001001 200']
### TEST DATA - efficiency
# num_b = 200000
# num_o = 10000

# def gen_item():
#     x = str(random.randint(1,10**9))
#     y = str(random.randint(1,10**4))
#     return str(x) + ' ' + str(y)

# buckets = [gen_item() for _ in range(num_b)]
# orders = [gen_item() for _ in range(num_o)]
### END TEST DATA


#Convert lists
buckets_colour = []
buckets_volume = []
for i in range(len(buckets)):
    buckets[i] = buckets[i].split()

buckets = sorted(buckets,key=lambda x:x[0])

for i in range(len(buckets)):
    buckets_colour.append(int(buckets[i][0]))
    buckets_volume.append(int(buckets[i][1]))
# for i in range(len(orders)):
#     orders[i] = list(map(int,orders[i].split()))

# t1 = time.time()

# print(orders)
# print(buckets)
# print(str(buckets_colour) + ' ' + str(buckets_volume))
# print('\n')

#Orders Loop
for _ in range(num_o):
    ##Second version: sorted lists, indexing, binary search
    # t3 = time.time()
    o = list(map(int,input().split()))
    try:
        index = binary_left(buckets_colour,o[0]-1000)
    except:
        print('no')
        continue
    
    # t4 = time.time()
    # print('search for index: ' + str(t4-t3))
    # steps = 0

    while index < len(buckets_colour) and buckets_colour[index] <= o[0]+1000 and o[1] >= 0:
        o[1] -= buckets_volume[index]
        index += 1
        # steps += 1

    # t5 = time.time()
    # print("iterate from index: " + str(t5-t4) + ' steps: ' + str(steps))
    
    #if order qty > 0 : fail : else : success
    if o[1] > 0:
        print('no')
    else:
        print('yes')
    # print('\n')

# tx = time.time()
# print('all the setup: ' + str(t1-t0))
# print('Full orders loop: ' + str(tx-t1))

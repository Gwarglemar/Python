# https://open.kattis.com/problems/chewbacca
# given a tree of out_degree with num_nodes, how many steps to get from node x to node y?

import sys, math

# first input: out_degree num_nodes num_q
x = list(map(int,input().split()))
num_nodes = x[0]
out_degree = x[1]
num_q = x[2]
    
#the case loop
for _ in range(num_q):
    case = list(map(int,input().split()))
    x = case[0]
    y = case[1]

    steps = 0

    x,y = (x-1,y-1) if x < y else (y-1,x-1)
    while(x!=y):
      y = math.ceil(y/out_degree) - 1
      x,y = (x,y) if x < y else (y,x)
      steps +=1
    print(steps)


#No longer necessary but I'm keeping these for later reference

# func for rounding to a given base.
def base_round(num, base = out_degree):
    return int(base*round(float(num)/base))

# func for getting all children of a given node-number
def get_children(num, base = out_degree):
    dif = base//2
    num = num*base
    output = []
    for x in range(0-dif,dif+1):
        output.append(num+x)
    return output
            
# https://open.kattis.com/problems/includescoring

# first input: number of contestants
num_c = int(input())

all_c = []
for i in range(num_c):
    all_c.append(list(map(int,input().split())))
    all_c[i].append(i) #store initial index

#list values: [0=solutions, 1=penalty, 2=end-time, 3=on-site, 4=original input index, 5=points earned]

#sort the list by the various keys/orders
all_c = sorted(sorted(sorted(all_c, key = lambda x:x[2]), key = lambda x:x[1]), key = lambda x:x[0], reverse = True)

#generate scores
points = [100,75,60,50,45,40,36,32,29,26,24,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
for i in range(len(all_c)):
    try:
        all_c[i].append(points[i])
    except:
        all_c[i].append(0)

#check for ties, update scores
sum = 0
tied = []
for i in range(num_c-1):
    if all_c[i][5] == all_c[i+1][5]:
        tied.append(i)
    else:
        for x in tied:
            all_c[x][5] = sum//len(tied)
        sum = 0
        tied = []
#catch for last iteration of previous for loop
if len(tied) > 0:
    tied.append(num_c-1)
    for x in tied:
        all_c[x][5] = sum//len(tied)

#sort back to original sort
all_c = sorted(all_c, key = lambda x:x[4])

#add point for on-site or not, and print
for i in range(num_c):
    all_c[i][5] += all_c[i][3]
    print(all_c[i][5])

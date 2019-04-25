# https://open.kattis.com/problems/calculatingdartscores

#input is a single integer
#output must be a set of at most 3 lines of how to get that score in darts, or else output "impossible"

#build our list of values
base = [[1,'single'],[2,'double'],[3,'triple']]
lookup = {}
for x in base:
    for num in range(1,21):
        # lookup.append([num*x[0],f'{x[1]} {num}'])
        try:
            lookup[num*x[0]] = f'{x[1]} {num}'
        except:
            pass

# func to get largest key value from dictionary to upper bound
def get_highest_val(upper_bound):
    if upper_bound >= 60:
        return (60, lookup[60])
    else:
        iter = upper_bound
        while iter > 0:
            try: 
                return (iter, lookup[iter])
            except:
                iter -= 1

#get input: single integer
score = int(input())

#TEST INPUTS: only output impossible values
# for x in range(1,180):
#     score = x

# ERRORS: 143 145 149 151 155 157 161 170 164 167
iter = 0
output=[]

while score != 0 and iter < 3:
    #some hard-coded fixes for some hard-to-calculate values.
    if iter == 1:
        if score == 97 or score == 91 or score == 85:
            high_val = get_highest_val(40)
        elif score == 89 or score == 83:
            high_val = get_highest_val(32)
        else:
            high_val = get_highest_val(score)
    else:      
        high_val = get_highest_val(score)

    score -= high_val[0]
    output.append(high_val[1])

    iter += 1

if score == 0:
    for x in output:
        print(x)
    # pass
else:
    print('impossible')
    # print(x)
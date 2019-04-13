#https://open.kattis.com/problems/batterup
#compute Slugging Percentage from 2 inputs: # at bats, and bases achieved from each respective at-bat.
#first input is a single integer representing the number of at bats
#second input is a series of integers representing the value of each respective at-bat
#an at-bat can have a value of -1 to 4:  walk/strikeout/single/double/triple/homerun respectively

import sys

result = -999999
while True:
    while True:
        # try/except for data validation
        try:
            num_at_bats = int(input("Enter the number of at-bats as a single integer: "))
        except:
            print("Invalid inputs. Please try again.")
        else:
            str_at_bats = input("Enter the full list of results for the at-bats as a space-separated list of integers from -1 to 4: ")
            break
    
    while True:
        #convert the str_at_bats to a list
        at_bats_data = str_at_bats.split()
        #more data validation
        if len(at_bats_data) != num_at_bats:
            print("number of at-bats doesn't match submitted number of inputs. Please try again.")
            break

        #now we take the data and do the math to get the percentage
        result = 0
        for num in at_bats_data:
            #also some data validation:
            try:
                num = int(num)
            except:
                print("Invalid inputs. Please try again.")
            
            result += int(num)
        break
    if result != -999999:
        break

print(result / num_at_bats)
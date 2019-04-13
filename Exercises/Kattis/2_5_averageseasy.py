#first input = num test cases
num_cases = int(input())

for _ in range(num_cases):
    #Each test case input preceded by blank line for some reason
    blank_line = input()
    
    #next input is 2 integers representing num CS students and num Econ students respectively
    temp = list(map(int, input().split()))
    num_cs = temp[0]
    num_econ = temp[1]

    #next inputs are the full lists of data
    cs_data = list(map(int, input().split()))
    econ_data = list(map(int, input().split()))

    ###test data
    # cs_data = [101,100,101,102,103,104]
    # econ_data = [98,99,100,102,101]

    #the math indicates (unless I'm way off base) that the correct answer is the number of students below the average of values in cs data that are also over the average of values in econ data, so let's find the averages

    cs_avg = sum(cs_data)/num_cs
    econ_avg = sum(econ_data)/num_econ

    #run the loop to get the number of cs students that match our expected requirements and output that number.
    #I wonder if sorting the list and just figuring out the break-point is faster; we'll try that if it goes over time.
    num_matches = 0
    for iq in cs_data:
        if iq < cs_avg and iq > econ_avg:
            num_matches += 1
    print(num_matches)
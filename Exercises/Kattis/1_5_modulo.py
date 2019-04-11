# Given two integers A and B, A modulo B is the remainder when dividing A by B. 
# For example, the numbers 7, 14, 27 and 38 become 1, 2, 0 and 2, modulo 3. 
# Write a program that accepts 10 numbers as input and outputs the number of distinct numbers in the input, if the numbers are considered modulo 42.

inputs = []
for _ in range(10):
    inputs.append(int(input())%42)

unique_inputs = set(inputs)

print(len(unique_inputs))
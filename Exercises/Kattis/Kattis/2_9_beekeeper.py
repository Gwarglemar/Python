#Given test cases, identify the word with the most double vowels

vowels = {'a','e','i','o','u','y'}
double_vowels = {'aa','ee','ii','oo','uu'}

while True:
    num_w = int(input())
    if num_w == 0:
        break

    words = []
    for _ in range(num_w):
        words.append(input())
    
    most_doubles = -1
    best_word = ''
    for w in words:
        index = 0
        double_count = 0
        while index < len(w)-1:
            if w[index] in vowels:
                if w[index+1] == w[index]:
                    double_count += 1
                    index += 2
                else:
                    index += 1
            else:
                index += 1
        if double_count > most_doubles:
            most_doubles = double_count
            best_word = w
            
    print(best_word)
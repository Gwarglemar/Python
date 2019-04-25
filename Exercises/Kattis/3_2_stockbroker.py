# https://open.kattis.com/problems/stockbroker

# init values
cash = 100
shares = 0
prices = []

#first input: num days (1-365)
num_days = int(input())


#next inputs: values on each day (1-500)
for _ in range(num_days):
    prices.append(int(input()))

for i in range(len(prices)-1):

    if prices[i] < prices[i+1]:
        #buy
        if (shares + (cash // prices[i])) > 100000:
            cash = cash - ((100000 - shares)*prices[i])
            shares = 100000
        else:
            shares += cash // prices[i]
            cash = cash % prices[i]

    elif prices[i] > prices[i+1]:
        #sell
        cash += shares * prices[i]
        shares = 0

if shares > 0:
    cash += shares * prices[-1]

print(cash)
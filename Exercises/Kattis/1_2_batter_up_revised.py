num_at_bats = int(input())
string_at_bats = map(int, input().split())

data = []
for item in string_at_bats:
	if item >= 0:
		data.append(item)

print(sum(data)/num_at_bats)
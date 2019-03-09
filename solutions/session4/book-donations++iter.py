titles = input().strip().split(',')

count = 0

for title in titles:
	it = iter(title.lower())
	if all(c in it for c in 'love'):
		count += 1
		
print(len(titles) if count >= 10 else count)
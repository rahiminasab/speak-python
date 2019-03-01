titles = input().strip().split(',')

count = 0

for title in titles:
	if all(c in iter(title.lower()) for c in 'love'):
		count += 1
		
print(len(titles) if count >= 10 else count)
cards = list(map(int, input().strip().split()))

q = []

for card in sorted(cards)[::-1]:
	if q:
		q.insert(0, q.pop())
	q.insert(0, card)

print(q)
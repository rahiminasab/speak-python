import collections

cards = list(map(int, input().strip().split()))

q = collections.deque()

for card in sorted(cards)[::-1]:
	if q:
		q.appendleft(q.pop())
	q.appendleft(card)

print(list(q))
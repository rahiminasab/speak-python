MIN_FREQ = 20
MAX_FREQ = 20000

n = int(input())

for _ in range(n):
	w, v = map(float, input().strip().split('#'))
	print(MIN_FREQ <= v/w <= MAX_FREQ)
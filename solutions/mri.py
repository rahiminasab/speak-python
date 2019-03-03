n = int(input())

max_area = 0
second_max_area = 0

for _ in range(n):
	a, b = map(int, input().split())
	
	area = a*b
	
	if area > max_area:
		second_max_area = max_area
		max_area = area
	elif area == max_area:
		continue
	elif area > second_max_area:
		second_max_area = area

print(second_max_area)
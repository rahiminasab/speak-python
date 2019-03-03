heights = list(map(float, input().strip().split(',')))

if not heights:
	print(0)

max_increase = 0
min_height = heights[0]

for i in range(1, len(heights)):
	if (heights[i] - min_height) > max_increase:
		max_increase = heights[i] - min_height
	elif heights[i] < min_height:
		min_height = heights[i]

print(max_increase)
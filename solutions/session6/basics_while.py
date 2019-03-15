# DO NOT convert num to string!
num = int(input().strip())

narcissistic_sum = 0

q, n = num, len(str(num))

while q > 0:
	q, r = divmod(q, 10)
	narcissistic_sum += r**n

print(num == narcissistic_sum)
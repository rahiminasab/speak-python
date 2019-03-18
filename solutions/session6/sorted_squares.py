nums = list(map(int, input().strip().split()))

l, r = 0, len(nums) - 1

res = [0]*len(nums)

while l <= r:
	if abs(nums[l]) > abs(nums[r]):
		res[r-l] = nums[l]**2
		l += 1
	else:
		res[r-l] = nums[r]**2
		r -= 1

print(res)
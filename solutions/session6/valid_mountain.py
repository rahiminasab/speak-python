nums = list(map(int, input().strip().split()))

l, r = 0, len(nums) - 1

while l < r and nums[l] < nums[l+1]:
	l += 1

while r > 0 and nums[r-1] > nums[r]:
	r -= 1

print(0 < l == r < len(nums)-1)
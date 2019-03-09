l1 = list(map(int, input().strip().split()))
l2 = list(map(int, input().strip().split()))

l3 = [] 

if len(l2) > len(l1):
    l1, l2 = l2, l1

i, carry = -1, 0

while -i <= len(l1) and -i <= len(l2):
    d = l1[i] + l2[i] + carry
    l3.insert(0, d % 10)
    carry = d // 10
    i -= 1

while -i <= len(l1):
    d = l1[i] + carry
    l3.insert(0, d % 10)
    carry = d // 10
    i -= 1

if carry > 0:
    l3.insert(0, carry)

print(l3)
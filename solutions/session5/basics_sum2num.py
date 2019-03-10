l1 = list(map(int, input().strip().split()))
l2 = list(map(int, input().strip().split()))

l3 = [] 

if len(l2) > len(l1):
    l1, l2 = l2, l1

carry =  0

for i in range(1, len(l2)+1):
    d = l1[-i] + l2[-i] + carry
    l3.append(d % 10)
    carry = d // 10

for i in range(len(l2)+1, len(l1)+1):
    d = l1[-i] + carry
    l3.append(d % 10)
    carry = d // 10

if carry > 0:
    l3.append(carry)

print(list(reversed(l3)))
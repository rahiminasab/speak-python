my_dict = {int(k): int(v) for k, v in map(lambda x: x.split(":"), input().strip().split())}

print(len(set(i for i in my_dict.values())))
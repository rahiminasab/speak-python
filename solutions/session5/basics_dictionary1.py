my_dict = {int(k): v for k, v in map(lambda x: x.split(":"), f.readline().strip().split())}

print(sum(len(my_dict[k]) for k in my_dict if k %2 == 0))
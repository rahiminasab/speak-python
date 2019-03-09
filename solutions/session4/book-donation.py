def is_subsequence(small, big):
    """
    
    :param small: an arbitrary string all lower cased
    :param big: an arbitrary string all lower cased
    :return: True iff small is a sub-sequence in big (i.e. you can find all the characters of small in big in order.
    """
    
    idx = 0  # the index of character in small that we want to match in big
    for c in big:
        # if we already matched all the characters in small,no need to exhaust remaining chars in big. so break.
        if idx == len(small):  
            break
        # if you can match the current char in small, then increase the idx to later match the next char in small.
        if c == small[idx]:
            idx += 1
    
    return idx == len(small)  # returns True if we could match all the chars in small.


titles = input().strip().split(',')

count = 0

for title in titles:
	if is_subsequence('love', title.lower()):
		count += 1
		
print(len(titles) if count >= 10 else count)
import re

pattern = re.compile('.*l.*o.*v.*e.*', re.IGNORECASE)

titles = input().strip().split(',')

count = sum(1 for _ in filter(lambda x: x is not None, [pattern.match(title) for title in titles]))

print(len(titles) if count >= 10 else count)
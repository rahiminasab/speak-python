nrows, ncols = map(int, input().split())
m1 = [list(map(int, input().split())) for _ in range(nrows)]
m2 = [list(map(int, input().split())) for _ in range(nrows)]

# compute m1+m2 and store it in m3 and then print m3
m3 = [[m1[i][j]+m2[i][j] for j in range(ncols)] for i in range(nrows)]

print(m3)
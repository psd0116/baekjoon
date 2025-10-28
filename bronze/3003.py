N = list(map(int, input().split()))

A = [1,1,2,2,2,8]
c = []

for i in range(len(N)):
    a = A[i] - N[i]
    c.append(a)

print(*c)
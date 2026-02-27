M = int(input())
N = int(input())
O = []

for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        O.append(i)

if len(O) == 0:
    print(-1)
else:
    print(sum(O))
    print(O[0])
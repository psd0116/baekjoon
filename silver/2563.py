N = int(input())

paper = [[0] * 100 for _ in range(100)]

for i in range(N):
    a, b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            paper[x][y] = 1

total = 0
for row in paper:
    total += sum(row)

print(total)


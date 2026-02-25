# 1 -> 1개
# 2~7 -> 6개
# 8~19 -> 12개
# 20~37 -> 18개
N = int(input())
if N == 1:
    print(1)
    exit()

result = 1

for i in range(1, N+1):
    result += 6 * i
    if result >= N:
        print(i+1)
        break
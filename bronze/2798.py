N, M = map(int, input().split())

B = list(map(int, input().split()))

max_sum = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            current_sum = B[i] + B[j] + B[k]
            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)
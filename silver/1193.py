N = int(input())
line = 1

while N > line:
    N = N - line
    line = line + 1

if line % 2 == 0:
    print(f"{N}/{line - N + 1}")
else:
    print(f"{line - N + 1}/{N}")
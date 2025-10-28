N = input()
a = 1
for i in range(len(N)):
    if N[i] != N[-i-1]:
        a = 0
if a == 0:
    print(a)
else:
    print(a)
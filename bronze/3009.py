x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

Q = 0
W = 0

if x[0] == x[1]:
    Q = x[2]
elif x[0] == x[2]:
    Q = x[1]
else:
    Q = x[0]

if y[0] == y[1]:
    W = y[2]
elif y[0] == y[2]:
    W = y[1]
else:
    W = y[0]

print(Q, W)
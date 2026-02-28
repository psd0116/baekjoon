import sys
    
input = sys.stdin.readline
    
n = int(input().strip())
    
if n == 1:
    input()
    print(0)
        
xs = []
ys = []
    
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
        
width = max(xs) - min(xs)
height = max(ys) - min(ys)
    
print(width * height)
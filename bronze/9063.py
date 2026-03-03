import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    
    if n == 1:
        print(0)
        return
        
    xs = []
    ys = []
    
    idx = 1
    for _ in range(n):
        xs.append(int(data[idx]))
        ys.append(int(data[idx+1]))
        idx += 2
        
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    
    print(width * height)

if __name__ == '__main__':
    solve()
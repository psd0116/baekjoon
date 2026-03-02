import sys

input = sys.stdin.readline
    
while True:
    line = input().strip()
    if not line:
        continue
            
    a, b, c = map(int, line.split())
        
    if a == 0 and b == 0 and c == 0:
        break
            
    sides = sorted([a, b, c])
        
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")

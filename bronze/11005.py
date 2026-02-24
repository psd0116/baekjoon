N, B = map(int, input().split())

result = ""
while N > 0:
    Z = N % B
    if Z < 10:
        result = str(Z) + result
    else:
        result = chr(ord("A") + Z - 10) + result
    N = N // B

print(result)
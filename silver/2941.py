N = input()

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

for i in a:
    N = N.replace(i,'1')
print(len(N))
# for i in a:
#     if N in i:
#         count += 1
# print(N)
# print(count)

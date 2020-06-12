number = int(input())
ans = 0
k = 1
bits = [3, 2, 1, 0]
for i in bits:
    if (1 << i) & number > 0: ans = ans + k
    k = k*2  
print(ans)

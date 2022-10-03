n = int(input())
e = []
res = []
for x in range(n):
    e.append(x)
print(e)
if len(e)%2==0:
    odd = e[n-2:0:-2]
    even = e[1:n-1:2]
    odd.append(e[0])
    even.append(e[n-1])
    print(odd)
    print(even)
    for x in range(int(n/2)):
        res.append(odd[x])
        res.append(even[x])
if len(e)%2!=0:
    odd = e[n - 1:0:-2]
    even = e[1:n - 1:2]
    odd.append(e[0])
    print(odd)
    print(even)
    for i in range(n):
        if i%2==0:
            res.append(odd[0])
            odd.pop(0)

        elif i%2!=0:
            res.append(even[0])
            even.pop(0)
print(res)

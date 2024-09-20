n = int(input("Son kiriting: "))
for i in range(1, n+1):
    n2 = "+".join(str(x) for x in range(1, i+1))
    print(f"{n2}={sum(range(1, i+1))}")

lst = [1, 2, 33, 5, 6, 7, 7]
kiritilgan_son = int(input("Son kiriting: "))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == kiritilgan_son:
            print(f"lst[{i}] + lst[{j}] = {kiritilgan_son} indexlar: {i} {j}")

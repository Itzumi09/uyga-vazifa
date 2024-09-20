n = int(input("Son kiriting: "))
count = 0
num = n + 1

while count < 5:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        count += 1
    num += 1

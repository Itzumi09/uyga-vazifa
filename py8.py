matn = input("Gap kiriting: ")
sozlar = matn.split()
result = [word[::-1] if len(word) % 2 != 0 else word for word in matn]
print(" ".join(result))

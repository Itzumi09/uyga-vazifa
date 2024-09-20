lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst = [t[:-1] + (100,) for t in lst]
print(lst)

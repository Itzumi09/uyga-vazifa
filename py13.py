lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
lst = sorted(lst, key=lambda x: float(x[1]), reverse=True)
print(lst)

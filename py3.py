list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

matn = sorted([x for x in list1 if type(x) == str])
boshqa = sorted([x for x in list1 if type(x) != str], reverse=True)

print("text =", matn)
print("boshqa =", boshqa)

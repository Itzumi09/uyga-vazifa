lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
lst = [t for t in lst if t]
print(lst)

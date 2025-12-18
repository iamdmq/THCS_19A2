d = {'a': 10, 'b': 50, 'c': 25}
max_key = max(d, key=d.get)
print("Key có giá trị lớn nhất:", max_key)
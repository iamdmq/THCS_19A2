lst = [1, 2, 3, 4, 5]
k = int(input("Nhập k: "))
k = k % len(lst) 
result = lst[-k:] + lst[:-k]
print("List sau khi dịch:", result)
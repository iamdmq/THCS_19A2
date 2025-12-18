s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
words = s.split()
result = [word for word in words if len(word) > n]
print("Các từ thỏa mãn:", result)
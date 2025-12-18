lst = [10, 20, 4, 45, 99, 99, 45]
unique_lst = list(set(lst)) # Loại bỏ trùng để tìm số lớn thứ 2 thực sự
unique_lst.sort()
print("Số lớn thứ hai là:", unique_lst[-2])
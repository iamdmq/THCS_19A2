matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
tong_phu = sum(matrix[i][n - 1 - i] for i in range(n))
print("Tổng đường chéo phụ:", tong_phu)
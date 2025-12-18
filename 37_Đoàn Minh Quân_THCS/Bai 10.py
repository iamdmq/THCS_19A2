matrix = [[1, 2, 3], [10, 11, 12], [4, 5, 6]]
max_row = max(matrix, key=sum)
print("Hàng có tổng lớn nhất:", max_row, "với tổng =", sum(max_row))
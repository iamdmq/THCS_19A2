A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
res = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
print("Kết quả nhân ma trận:", res)
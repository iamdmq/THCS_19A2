matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
print("Ma trận đối xứng:", is_symmetric)
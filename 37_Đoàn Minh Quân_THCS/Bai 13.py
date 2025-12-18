def is_identity(m):
    n = len(m)
    for i in range(n):
        if len(m[i]) != n: return False
        for j in range(n):
            if (i == j and m[i][j] != 1) or (i != j and m[i][j] != 0):
                return False
    return True
lst = [1, 2, 2, 3, 1, 4, 5, 2]
seen = set()
result = []
for x in lst:
    if x not in seen:
        result.append(x)
        seen.add(x)
print("Danh sách sau khi lọc:", result)
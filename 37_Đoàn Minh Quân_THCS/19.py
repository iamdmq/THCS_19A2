data = {'An': 8, 'Bình': 7, 'Chi': 8, 'Đông': 9}
grouped = {}
for ten, diem in data.items():
    if diem not in grouped:
        grouped[diem] = []
    grouped[diem].append(ten)
print("Nhóm theo điểm:", grouped)
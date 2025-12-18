d = {'sp1': 100, 'sp2': 30, 'sp3': 80}
filtered_d = {k: v for k, v in d.items() if v > 50}
print("Các cặp có giá trị > 50:", filtered_d)
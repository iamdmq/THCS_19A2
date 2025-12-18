s = input("Nhập chuỗi: ")
chu_cai = chu_so = dac_biet = 0
for char in s:
    if char.isalpha(): chu_cai += 1
    elif char.isdigit(): chu_so += 1
    else: dac_biet += 1
print(f"Chữ cái: {chu_cai}, Chữ số: {chu_so}, Đặc biệt: {dac_biet}")
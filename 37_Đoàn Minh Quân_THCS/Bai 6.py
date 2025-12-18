lst = [1, 2, 3, 4, 5, 6]
tong_chan = sum(x for x in lst if x % 2 == 0)
tong_le = sum(x for x in lst if x % 2 != 0)
print(f"Tổng chẵn: {tong_chan}, Tổng lẻ: {tong_le}")
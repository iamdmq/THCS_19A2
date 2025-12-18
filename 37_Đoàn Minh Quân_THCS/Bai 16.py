s = "hello world"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Tần suất:", freq)
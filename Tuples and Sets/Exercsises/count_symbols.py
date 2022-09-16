text = input()

symbols_count = {}

for char in text:
    if char not in symbols_count:
        symbols_count[char] = text.count(char)

[print(f"{key}: {symbols_count[key]} time/s") for key in sorted(symbols_count)]

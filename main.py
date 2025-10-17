letters = 0    # 英文字符计数
digits = 0     # 数字计数
spaces = 0     # 空格计数
others = 0     # 其他字符计数
line = input()
for char in line:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")

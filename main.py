text = input("请输入一行字符：")

letters = digits = spaces = others = 0

for char in text:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1
    elif '0' <= char <= '9':
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print("英文字符:", letters)
print("数字:", digits)
print("空格:", spaces)
print("其他字符:", others)

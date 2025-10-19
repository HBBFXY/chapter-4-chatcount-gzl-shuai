# charcount.py
text = input()
letters = digits = spaces = others = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print("英文字符:", letters)
print("数字:", digits)
print("空格:", spaces)
print("其他字符:", others)

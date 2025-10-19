# charcount.py
def char_count(text):
    letters = digits = spaces = others = 0
    
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
            
    return letters, digits, spaces, others

if __name__ == "__main__":
    text = input()
    letters, digits, spaces, others = char_count(text)
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

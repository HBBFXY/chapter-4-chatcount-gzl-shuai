# main.py
def count_characters(text):
    """
    统计字符串中各类字符的数量
    """
    letters = 0  # 英文字符
    digits = 0   # 数字
    spaces = 0   # 空格
    others = 0   # 其他字符
    
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

def main():
    text = input()
    letters, digits, spaces, others = count_characters(text)
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

if __name__ == "__main__":
    main()

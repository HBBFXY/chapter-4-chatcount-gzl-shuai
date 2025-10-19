
def count_characters():
    try:
        # 从键盘输入一行字符
        text = input("请输入一行字符：")
        
        # 初始化计数器
        letters = 0  # 英文字符
        digits = 0   # 数字
        spaces = 0   # 空格
        others = 0   # 其他字符
        
        # 遍历每个字符并进行分类统计
        for char in text:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                others += 1
        
        # 输出统计结果
        print(f"英文字符: {letters}")
        print(f"数字: {digits}")
        print(f"空格: {spaces}")
        print(f"其他字符: {others}")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    count_characters()

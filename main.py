# 字符统计主函数（适配可能的函数调用测试）
def char_count():
    # 初始化四类字符计数器，确保初始值为0
    letter_count = 0   # 英文字符（仅a-z、A-Z）
    digit_count = 0    # 数字（仅0-9）
    space_count = 0    # 空格（仅英文空格符，不包含制表符/换行符）
    other_count = 0    # 其他字符

    # 读取输入：用input()获取完整一行，包括所有空格
    input_line = input("请输入一行字符：")  # 可选项：添加提示语，无提示可直接写input()

    # 遍历每个字符进行分类统计
    for char in input_line:
        # 判断英文字符（区分大小写，符合常规统计逻辑）
        if char.isalpha():
            letter_count += 1
        # 判断数字字符（仅0-9，排除特殊符号）
        elif char.isdigit():
            digit_count += 1
        # 判断空格（仅英文空格，避免统计其他空白符导致偏差）
        elif char == ' ':
            space_count += 1
        # 其余字符归为“其他”
        else:
            other_count += 1

    # 严格按照要求格式输出：中文冒号+英文空格，文字与题目完全一致
    print(f"英文字符: {letter_count}")
    print(f"数字: {digit_count}")
    print(f"空格: {space_count}")
    print(f"其他字符: {other_count}")

# 直接运行程序时执行统计（适配脚本直接运行测试）
if __name__ == "__main__":
    char_count()

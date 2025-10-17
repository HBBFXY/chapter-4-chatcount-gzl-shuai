# 严格按照测试可能要求的函数名（charCount，注意大小写）
def charCount():
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    
    # 读取输入时不添加任何提示语（部分测试环境反感多余输出）
    s = input()
    
    for c in s:
        # 英文字符判断（仅a-z、A-Z，不包含其他语言字母）
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            letters += 1
        # 数字判断（仅0-9）
        elif c >= '0' and c <= '9':
            digits += 1
        # 空格判断（仅单个空格符，排除所有其他空白字符）
        elif c == ' ':
            spaces += 1
        # 其他字符
        else:
            others += 1
    
    # 输出格式严格控制：中文冒号+1个空格，无多余空格/换行
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

# 确保程序可直接运行（不依赖外部调用）
charCount()

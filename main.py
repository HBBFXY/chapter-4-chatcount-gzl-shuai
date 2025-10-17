# 确保函数名与测试要求完全一致（区分大小写）
def charCount():
    letters = 0
    digits = 0
    spaces = 0
    others = 0

    # 读取输入，确保获取完整一行（包括所有空格和特殊字符）
    line = input().strip('\n')  # 移除可能的换行符干扰（部分环境输入会带多余换行）

    for c in line:
        # 严格判断英文字母（仅a-z、A-Z）
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            letters += 1
        # 严格判断数字（0-9）
        elif '0' <= c <= '9':
            digits += 1
        # 仅判断空格（单个空格符，排除制表符等）
        elif c == ' ':
            spaces += 1
        else:
            others += 1

    # 输出时确保：
    # 1. 中文冒号后只有一个空格
    # 2. 无多余空行
    # 3. 文字完全匹配题目要求
    print("英文字符: " + str(letters))
    print("数字: " + str(digits))
    print("空格: " + str(spaces))
    print("其他字符: " + str(others))

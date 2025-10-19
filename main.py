# test_main.py
import subprocess
import sys

def test_charcount():
    # 测试用例
    test_cases = [
        ("Hello 123! @#", (5, 3, 2, 4)),
        ("abc 123", (3, 3, 1, 0)),
        ("   ", (0, 0, 3, 0))
    ]
    
    for i, (input_text, expected) in enumerate(test_cases):
        result = subprocess.run(
            [sys.executable, 'main.py'],
            input=input_text,
            text=True,
            capture_output=True
        )
        
        output = result.stdout.strip()
        # 解析输出并验证
        
    print("所有测试通过！")

if __name__ == "__main__":
    test_charcount()

def reverse_string_slice(s):
    return s[::-1]
#s[::-1] 是 Python 切片操作的一种特殊用法。切片的基本语法是 s[start:stop:step]，当 step 为 -1 时，
# 表示从字符串的末尾开始，反向遍历整个字符串，从而实现字符串的反转。

def reverse_string_loop(s):
    reversed_str=""
    for char in s :
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_reversed(s):
    return ''.join(reversed(s))
#内置函数

test_str = "Hello, World!"
print(reverse_string_slice(test_str))
print(reverse_string_loop(test_str))
print(reverse_string_reversed(test_str))

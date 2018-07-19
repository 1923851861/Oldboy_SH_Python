import random

# 1X3Y3ZX
def make_code(size=7):
    res = ''
    for i in range(size):
        # 循环一次则得到一个随机字符（字母/数字）
        s = chr(random.randint(65, 90))
        num = str(random.randint(0, 9))
        res += random.choice([s, num])
    return res


res=make_code()
print(res)
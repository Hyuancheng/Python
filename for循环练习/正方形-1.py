
#绘制一个有两条对角线的正方形（下列方法为根据图形特点总结得出，更好的方法为建立直角坐标系，借助直线方程简练地达到目的）
n = 8
# 当n为偶数时
if n % 2 == 0:
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("* " * n, end="")
            print()
        # 上半部分
        elif i > 1 and i <= n / 2:
            print("* ", end="")
            print("  " * (i - 2), end="")  # 新增
            print("* ", end="")  # 新增
            print("  " * (n - 1 - i - (i - 1)), end="")  # 改动
            print("* ", end="")
            print("  " * (i - 2), end="")
            print("* ")
        # 下半部分
        elif i > n / 2 and i < n:
            print("* ", end="")
            print("  " * (n - 1 - i), end="")  # /
            print("* ", end="")  # /
            print("  " * (2 * i - n - 2), end="")  # \
            print("* ", end="")  # \
            print("  " * (n - i - 1), end="")
            print("* ")

# 当n为奇数时
if n % 2 == 1:
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("* " * n, end="")
            print()
        # 上半部分
        elif i > 1 and i <= n / 2:
            print("* ", end="")
            print("  " * (i - 2), end="")  # 新增
            print("* ", end="")  # \新增
            print("  " * (n - 1 - i - (i - 1)), end="")  # 改动
            print("* ", end="")  # /
            print("  " * (i - 2), end="")
            print("* ")
        # 两线交点时
        elif i > n / 2 and i < n / 2 + 1:
            print("* ", end="")
            print("  " * (n - 1 - i), end="")
            print("* ", end="")
            print("  " * (i - 2), end="")  # n-1-2-n+1+i
            print("* ")
        # 下半部分
        elif i > n / 2 + 1 and i < n:
            print("* ", end="")
            print("  " * (n - 1 - i), end="")  # /
            print("* ", end="")  # /
            print("  " * (2 * i - n - 2), end="")  # \
            print("* ", end="")  # \
            print("  " * (n - i - 1), end="")
            print("* ")

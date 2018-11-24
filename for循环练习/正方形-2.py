#通过建立坐标系(以左下角顶点为坐标原点),绘制带有两条对角线的正方形.
bianchang = 5
n = bianchang - 1
for y in range(n,-1,-1):
    for x in range(0,n+1):
        if x == 0 or x == n or y == 0 or y == n:
            print("* ",end="")
        elif x == y or x+y == n:
            print("* ",end="")
        else:
            print("  ",end="")
    print("")

#为正方形进行填充
bianchang = 15
n = bianchang - 1
for y in range(n,-1,-1):
    for x in range(0,n+1):
        if x == 0 or x == n or y == 0 or y == n:
            print("* ",end="")
        elif x == y or x+y == n:
            print("* ",end="")
        elif y < x and y > -x+n: #新增为图形进行填充
            print("* ",end="")
        else:
            print("  ",end="")
    print("")
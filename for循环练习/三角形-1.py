#打印中空倒三角形
n = 5
for i in range(1,n+1):
    if i == 1 or i == n or i == n-1:
        print("* " * (n+1-i),end="")
        print()
    else:
        print("* ",end="")
        print("  " * (n-1-i),end="")
        print("* ")


#可以利用双层for循环分别对行和列进行操作
n = 5
for i in range(n,0,-1):#此处决定行数
    for j in range(i):#决定列数
        if j == 0:
            print("* ",end="")#第一列为全打印
        elif i == n:
            print("* ",end="")#第一行也为全打印
        elif j == i-1:
            print("* ",end="")#即每一行最右侧位置打印
        else:
            print("  ",end="")#其余位置用空格填充
    print()

"""__author__ = 余婷"""

"""
1.变量
变量名 = 值

python中所有的变量都是保存数据的地址， 使用的是地址对应的值

值，地址，类型
"""
num = 10
num1 = num2 = num3 = 100
num11, num12, num13, num14 = 1, 2, 3, 4
print(num)
num = 'abc'
print(num)

"""
2.运算符：数学，比较，逻辑，赋值，位运算
数学: +, -, *, /, %, //, **
比较: >, <, ==, !=, >=, <=
逻辑: and, or, not
and短路操作：如果and前面的条件为False,and后面的条件语句不会执行
or短路操作：如果or前面的条件为True,or后面的条件语句不会执行
赋值: =, +=, -=, *= ....
变量 += 值  # 变量=变量+值
位运算：&，|，^, ~, <<, >>
"""
print(5 // 2)

# 注意：整除的时候，如果商是负的小数(小数点后的值大于0)，最后的结果是整数部分减1
print(-5 // 2)
print(-4.2 // 2)

# 注意：支持像数学中的方式去使用>,<,>=,<=去表示范围
num = -10
print(0 < num < 10)

# num要大于等于0并且小于等于10
print(0 <= num <= 10)



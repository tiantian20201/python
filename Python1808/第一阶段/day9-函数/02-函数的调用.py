"""
函数在声明的时候不会执行函数体,只有在调用函数的时候才会执行函数体
"""


def say_hello():
    print("hello")


# 1.函数的调用过程（重点）
"""
def 函数名（形参）：
    函数体

函数名（实参）

a.物理过程
第一步：回到函数声明的位置
第二步：用实参给形参赋值（传参）；要保证每个形参都有值
第三步：执行函数体
第四步：获取返回值
第五步：回到函数调用的位置

b.函数调用的过程是一个压栈的过程
当函数调用的时候，系统会自动在内存中栈区间开辟空间，存储函数调用过程中产生的数据
（这的数据包括参数和在函数的声明的变量）。当函数调用完成后，对应的内存空间会自动销毁。

"""
a = 10
b = 20


def change(a, b):
    a, b = b, a
    print(a, b)  #20 10

change(a, b)
print("函数外", a, b)  #函数外 10 20

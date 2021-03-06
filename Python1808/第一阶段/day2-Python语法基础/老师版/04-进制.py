"""__author__ = 余婷"""

# 1.十进制
"""
a.基数：0，1，2，3，4，5，6，7，8，9
23
123
90
89
77677676

b.进位：逢10进1
c.位权：123 = 1*10^2 + 2*10^1 + 3*10^0  (10^n)

d.表示: 所有的数字都是10进制数（数字直接写）
"""
123
10
78
67

# 2.二进制
"""
a.基数: 0，1
011011010001001001
111010101

b.进位: 逢2进1
1+0 = 1
0+1 = 1
0+0 = 0
1+1 = 0 -- 进1
110 + 011 = 1001
101+110 = 1011

c.位权: 1101(2) = 1*2^0 + 0*2^1 + 1*2^2 + 1*2^3 = 13  (2^n)

d.表示: 在二进制数前加前缀：0b或者0B
"""
0b10101
0B01010
# 0b2100  # SyntaxError: invalid syntax

# 3.八进制
"""
a.基数：0，1，2，3，4，5，6，7
67
12
106465
b.进位：逢8进1
c.位权: 123(8) = 3*8^0 + 2*8^1 + 1*8^2 =  83   (8^n)

d.表示:在八进制数加前缀：0o或者0O
"""
0o12
0O67

# 4.十六进制
"""
a.基数:0，1，2，3，4，5，6，7，8，9，a(10)，b(11)，c(12)，d(13)，e(14)，f(15)
字母大写和小写都可以

123
12a
ff
ef
abc
abc12

b.进位：逢16进1
c.位权: 123(16) = 3*16^0 + 2*16^1 + 1*16^2  (16^n)

d.表示: 在十六进制数的前面加前缀：0x或者0X
"""
0x12a
0Xffee
0X1023

num = 0x1010
print(num)


# 5.其他进制和十进制之间的转换
"""
a.其他进制转十进制：每一位上的数*权值，然后再求和
110(2) = 1*2^1 + 1*2^2 = 6(10)
110(8) = 1*8^1 + 1*8^2 = 72(10)
110(16) = 1*16^1 + 1*16^2 = 272(10)

b.将十进制转换成其他进制
100(10) = 1100100(2)
100(10) = 144(8)
100(10) = 64(16)

79(10) = 1001111(2)
79(10) = 117(8)
79(10) = 4f(16)
"""

# 6. 二进制和八进制十六进制的相互转换
"""
a.二进制转八进制：每3位的二进制转换成1位的八进制
001100100110010011100(2) = 1446234(8)

八进制转二进制：每1位8进制，转换成3位的二进制
6745(8) = 110 111 100 101(2)

b.二进制转十六进制：每4位的二进制转换成1位的十六进制
0110 0100 1100 1001 1100(2) = 64c9c(16)

十六进制转二进制：每1位16进制，转换成4位的二进制
6745(16) = 0110 0111 0100 0101(2)
a12(16) = 1010 0001 0010(2)
"""

# 7.进制转换相应的函数 - 返回值是字符串
"""
bin(数字)  - 将数字转换成2进制
"""
print(bin(100))
print(bin(0x6745))
print(bin(0o76))

"""
oct(数字) - 将数字转换成8进制
"""
print(oct(100))
print(oct(0x1af))
print(oct(0b110001101))

"""
hex(数字) - 将数字转换成16进制
"""
print(hex(100))
print(hex(0o67))
print(hex(0b11011101110))

"""
所有进制最后会自动转换成10进制
"""
num = 0xaf
print(num)

print(0b111 + 0b110)
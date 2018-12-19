"""
1.什么是模块
python 中一个py文件就是一个模块

2.怎么关联多个模块
方式一：
import  模块名 - 将指定的模块导入到当前模块中（模块名就是py文件的文件名）

说明：
a.执行import的时候，实质会进入指定的模块对应的py文件中，去执行里面的代码
b.导入之前会查重，如果已经导入就不会再导入了
c.通过import去导入一个模块后。可以通过  模块名.全局变量  去使用被导入的模块中的内容


"""
import test1
import test2
#使用test1中的变量
a=test1.test1_
print(a)

#调用test1中的函数
test1.test1_func1()

"""
方法2：
form  模块名 import 变量/函数名 - 导入模块中指定的变量或者函数

说明：
a.执行到导入模块的语句时，还是会先执行指定模块中的所有语句
b.通过form - import导入的时候，还是会查重，如果导入过就不会执行。
c. 使用的时候只能用import后面的变量/函数，而且用的时候不用再前面加模块名
d.import后面可以使用逗号将多个变量导入，也可以加*将模块中使用的全局变量都导入。

"""


"""
函数 - 对功能进行封装 - 获取当前时间对于的代码段封装在函数中
模块 - 对多个功能和多个数据进行封装 - 将使用和时间相关的函数或变量放在一个py文件中。
包 - 对多个模块进行封装  - 将所有与时间相关的py文件放在一个包里面。
什么是包:含有__init__.py文件的文件夹


3.重命名
form  模块名  import  as  新模块名
import 模块名 as  新模块名

"""

"""
4.包的导入
import  包名  会直接执行包中的__init__.py文件中的代码
import  包名.模块名 - 将包中的指定模块

form 包名 import 模块名
form  包名.模块名 import 变量
"""

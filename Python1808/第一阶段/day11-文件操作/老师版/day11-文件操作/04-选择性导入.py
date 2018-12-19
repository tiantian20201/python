"""__author__ = 余婷"""

"""
在模块中将不需要其他模块导入和执行的代码写到 if __name__ == '__main__'语句中。
这样就可以阻止代码被其他模块执行

原理：每个模块都有一个__name__属性，默认值是模块对应的py文件的名字。
当正在直接执行模块的时候，模块的__name__属性值就会变成'__main__'。
当import模块的时候，执行模块，模块的__name__属性不是'__main__'
"""

import test1

# print(test1.test1_a)

if __name__ == '__main__':
    # 写在这儿的代码不会被其他模块执行; 声明在这儿的变量也不会被其他模块导入
    print('')


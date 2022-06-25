import sys
from os import path

# 상대경로
# from .calculator.add_and_multiply import add_and_multiply

# 절대경로
from calculator.add_and_multiply import add_and_multiply

if __name__ == '__main__':
    print(add_and_multiply(1, 2))

# import os
# print(os.getcwd())  # /Users/hhj/Desktop/gitHub/Python/Replit_Python

# print(__name__)
# print(add_and_multiply.__name__)

# sys.path.insert(1, path.abspath('./calculator'))
# print(path.abspath('./calculator'))


sys.path.insert(1, '/Users/hhj/Desktop/gitHub/Python/Replit_Python/calculator')
print(sys.path)

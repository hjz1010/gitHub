
# from os import path
# import sys

# 상대경로
# from .multiplication import multiply

# 절대경로
from multiplication import multiply


def add_and_multiply(a, b):
    return multiply(a, b) + (a+b)


# print(os.getcwd())  # /Users/hhj/Desktop/gitHub/Python/Replit_Python
# sys.path.insert(1, path.abspath('.'))
# sys.path.append(path.abspath('..'))
# print(path.abspath('.'))
# print(sys.path)
# print(__name__)

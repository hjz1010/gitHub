#!/usr/bin/env python3

# 별찍기 - 크리스마스 트리 - Python
'''
print(' ' * (n-1) + '*' * 1 )
print(' ' * (n-2) + '*' * 3 )
print(' ' * (n-3) + '*' * 5 )
print(' ' * (n-4) + '*' * 7 )
print(' ' * (n-5) + '*' * 9 )
'''


def tree():
    n = int(input("원하는 트리의 사이즈를 입력하세요: "))
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))


def tree2():
    n = int(input("원하는 트리의 사이즈를 입력하세요: "))
    for i in range(1, n+1):
        star = '*' * (2*i-1)
        print(star.center(2*n-1))


if __name__ == "__main__":
    tree2()


# https://www.delftstack.com/ko/howto/python/python-pad-string-with-spaces/

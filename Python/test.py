# -*- coding: utf-8 -*-

# mel = {'name': 'HHJ', 'age': 33, 'job': 'programmer'}

# mel.update({'birth': '1988.10.10'})


# data = {}

# # key로 'a'를 추가학 value 0을 설정함, setdefault는 현재 value 값을 리턴
# ret = data.setdefault('a', 0)
# # print(ret, data)

# ret = data.setdefault('a', 1)   # 이미 key가 있는 경우 setdefault 현재 value 값을 리턴
# print(ret, data)

# name = ['Mel', 'Jay', 'Ahkim']
# age = [33, 30, 32]
# # print(zip(name, age))
# a = dict(zip(name, age))
# # print(a)

# b = {k: v+30 for k, v in zip(a.keys(), a.values())}
# print(b)

# _list = []
# print(_list[-1])

import datetime
from ast import Num
import math
from collections import namedtuple
from re import A


# a = 3
# mystr = f"{a:5d}"
# print(mystr)

# print('this is {0:<10} | done {1:<5} |'.format('left', 'a'))
# print('this is {0:>10} | done {1:>5} |'.format('right', 'b'))
# print('this is {0:^10} | done {1:^5} |'.format('center', 'c'))

# name = 'Mel'
# score = 99.5
# print(f"|{name:10}의 점수는 |{score:10} 점입니다.")

# print('정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12))
# print('소수 아래 3자리 : {0:0.3f},{1:0.3f}'.format(1.12345, 1.1))

# print([i*i if i % 2 == 0 else i for i in range(10)])

# book = namedtuple('book', ['title', 'price'])
# mybook = book('Python', 28000)
# print(mybook.title, mybook.price)

# a = (1, 2, 3, 4)
# b = set(a)
# print(b)
# print(i for i in b)


# 파이썬 100제 #1~30

# 2
l = [200, 100, 300]
l.insert(2, 10000)
# print(l)

# 7
# 파이썬에서 변수의 이름은
# - 대문자(A-Z)와 소문자(a-z)
# - 숫자(0-9)
# - 밑줄(_)
# - 단, 숫자로 시작할 수는 없다.
# - 예약어는 변수명으로 사용할 수 없다.

# 9
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

# print(year, month, day, sep='/', end=' ')
# print(hour, minute, second, sep=':')

# 10


def tree():
    n = int(input("원하는 트리의 사이즈를 입력하세요: "))
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))


def tree2():
    n = int(input("원하는 트리의 사이즈를 입력하세요: "))
    for i in range(1, n+1):
        star = '*' * (2*i-1)
        print(star.center(2*n-1))

# 12


class Wizard():
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')


# x = Wizard(health=545, mana=210, armor=10)
# print(x.health, x.mana, x.armor)
# x.attack()

# 13
# n = int(input("몇 번째 행성을 보여드릴까요? : "))
# planetList = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
# print(planetList[n-1])

# # 14
# n = int(input("숫자를 입력하세요: "))
# result = '짝' if n % 3 == 0 else n
# print(result)

# # 15
# name = input('자기소개:')
# print(f'안녕하세요. 저는 {name}입니다.')

# 16
# inputSen = input('문장을 입력하세요: ')
# print(inputSen[::-1])

# # 17
# height = int(input('키를 입력하세요: '))
# print('Yes' if height >= 150 else 'No')

# 18
# scores = [int(i) for i in input('세 과목의 점수를 입력하세요: ').split()]
# avrg = sum(scores) // len(scores)
# print(avrg)

# 20
# a, b = list(map(int, input('두 숫자: ').split()))
# print(a//b, a % b)

# 21 다음 중 set을 만드는 방법이 아닌 것?

# 1)  x = {1, 2, 3, 5, 6, 7}
# 2)  x = {}
# 3)  x = set('python')
# 4)  x = set(range(5))
# 5)  x = set()

# 23 print(10/2)의 출력 결과는 5이다.(O/X)


# def foo(a, b, c):
#     print(a+b+c)


# data = [1, 2, 3]
# foo(*data)

# x = ['a', 'b']
# y = 'python'
# x.extend(y)
# print(x)

def outer(num):
    def inner():
        print(num)
    return inner


class outer2:
    def __init__(self, num):
        self.num = num

    def __call__(self):
        print(self.num)


# f2 = outer2(3)
# f2()
# f1 = outer(4)
# f1()

class foo():    # foo는 클래스
    def func(self, num):   # func는 메서드
        foo.name = "melony"
        self.num = num
        print(foo.name, self.num)


# f = foo()   # f는 인스턴스
# f.func(3)

class parent():
    def can_sing(self):
        print("Sing a song!")


father = parent()


class luckyChild(parent):
    pass


child1 = luckyChild()
# child1.can_sing()


class luckyChild2(parent):
    def can_dance(self):
        print("Shuffle dance!")


# child2 = luckyChild2()
# child2.can_sing()
# child2.can_dance()

class Point():
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        print((self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# point1 = Point((0, 0))
# point1.setx(1)
# point1.sety(2)
# point1.move(2, 3)
# point1.get()


# class Stock():
#     market = "kospi"

# print(max([-5, 0, 2, 4, 1], key=lambda x: x % 3))

# _list = [1, 2, 3, 4, 5]
# print(sum(_list[:5]))


# n = 25
# print(math.sqrt(n))
# print(math.floor(math.sqrt(n)))

# _num = input()
# _str = str(_num)
# print(len(_str))
# for i in len

# n = int(123.2)
# print(n)
# print(type(n))

# a = '12345'
# print(sum(map(int, a)))

# l = [1, 2, 3]
# [*a, b, c, d] = l
# print(a, b, c, d)
# def prime_num():
#     n = int(input("숫자: "))
#     for i in range(2, math.floor(math.sqrt(n))+1):
#         if n % i == 0:
#             return "NO"
#     return "YES"


# print(prime_num())

def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while (그룹_하나) and (그룹_둘):
        if (그룹_하나[0] < 그룹_둘[0]):
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값


주어진리스트 = [180, 145, 165, 45, 170, 175, 173, 171]
# 빈칸을 채워주세요

# print(병합정렬(주어진리스트))


def 퀵정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    if 입력리스트의길이 <= 1:
        return 입력리스트
    기준값 = 입력리스트.pop(입력리스트의길이//2)  # point를 리스트 중간쯤에 있는 값으로
    그룹_하나 = []
    그룹_둘 = []

    for i in range(입력리스트의길이-1):
        if 입력리스트[i] < 기준값:
            그룹_하나.append(입력리스트[i])
        else:
            그룹_둘.append(입력리스트[i])
    return 퀵정렬(그룹_하나) + [기준값] + 퀵정렬(그룹_둘)


# 주어진리스트 = input().split(' ')
# 주어진리스트 = list(map(int, 주어진리스트))

# print(퀵정렬(주어진리스트))

def bracketCheck():
    # 각 괄호의 쌍이 맞는지, 갯수 확인
    _input = input("괄호: ")
    result = True
    if _input.count("(") != _input.count(")"):
        result = False
    if _input.count("{") != _input.count("}"):
        result = False
    if _input.count("[") != _input.count("]"):
        result = False
    print(result)


def bracketCheck2():
    # 여는 괄호가 나오면 닫는 괄호를 확인하기
    _input = input("괄호: ")
    count = 0
    for a, b in [("(", ")"), ("{", "}"), ("[", "]")]:
        for txt in _input:
            if txt == a:
                count += 1
            if txt == b:
                if count == 0:
                    return False
                else:
                    count -= 1
        if count != 0:
            return False
    return True


def bracketCheck4():
    _input = input("괄호: ")
    openBrac = "({["
    closeBrac = ")}]"
    _list = []
    for txt in _input:
        if txt in openBrac:
            _list.append(txt)
        if txt in closeBrac:
            if closeBrac.find(txt) == openBrac.find(_list[-1]):   # index와 find
                _list.pop()
            else:
                return False
    if _list:
        return False
    else:
        return True


# def stamp():
#     inputList = map(int, input("스탬프: ").strip().split())
#     inputList = sorted(inputList)
#     startNum = inputList[0]
#     if inputList == list(range(startNum, startNum+len(inputList))):
#         return "YES"
#     return "NO"


# if __name__ == "__main__":
#     print(stamp())

# dict = {1: 4, 2: 5, 3: 6, "a": "b"}
# a = dict.pop("a")
# print(dict, a)

# a = '123456'
# b = a[-3:]
# c = a[:-3]
# print("b=", b, "c=", c)
# print(len(c))
# print(b+','+c)

# print('this is {0:^10} | done {1:+^5} |'.format('center', 'c'))


# hi = "Hello, World!"
# print(hi)
# print(hi.replace("H", ""))
# print(hi.translate(str.maketrans("HW", "  ")))

# N = 12
# print((N-2)*(N-1) / 2)
# print((N-1)*N / 2)

# a = datetime.date(2020, 7, 18)
# b = datetime.date(2020, 12, 23)
# print((a-b).days)
# # .strftime("%Y/%m/%d")
# d = "12:40"
# d = datetime.datetime.strptime(d, "%H:%M")
# print(d.strftime("%H:%M"))

# a = "12:30"
# a = datetime.datetime.strptime(a, "%H:%M")

# c = d-a
# print(c.days)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a+b*2
# print(c)

a = ([1, 2],
     [2, 4])
b = ([1, 0],
     [0, 3])
# print(len(a[0]))
# print(len(b))

c = []
if len(a) == len(b[0]):
    for i in range(len(a)):     # 모든 요소가 0 인 결과 행렬을 만들어두고
        c.append([0]*len(b[0]))
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(len(a[i])):
                c[i][j] += a[i][k] * b[k][j]   # 반복마다 요소를 바꿈
    print(c)
else:
    print(1)

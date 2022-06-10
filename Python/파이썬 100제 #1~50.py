# -*- coding: utf-8 -*-

import math
import datetime
from datetime import timedelta
import time
from curses.ascii import islower, isupper

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

# # 24
# inputName = input('참가자명을 입력해주세요: ')
# print(inputName.upper())

# 25
# def circle(n=int(input('원의 반지름: '))):
#     return n*n*3.14

# print(circle())

# 26


def planetInEng():
    K = input("행성 이름: ")
    planets = {
        '수성': "Mercury", '금성': "Venus", '지구': "Earth", '화성': "Mars", '목성': "Jupiter",
        '토성': "Saturn", '천왕성': "Uranus", '해왕성': "Neptune"
    }
    print(planets[K])

# 27


# stuNames = input('학생들 이름: ').split()
# stuScores = input('점수: ').split()
# stuDict = dict(zip(stuNames, stuScores))
# print(stuDict)

# 28


def twoGram():
    _input = input('문자열을 입력해주세요: ')
    for i in range(len(_input)-1):
        print(_input[i]+_input[i+1])

# 29


def upperCase():
    _input = input('알파벳을 입력하세요: ')
    result = ''
    for letter in _input:
        if letter.isupper():
            result += letter

    return "Perfect!" if result == _input else result
# print(upperCase())

# 30


def findString():
    sentence = input('문장: ')
    word = input('단어: ')
    return sentence.find(word)


print(findString())


# 6/2 Python100제 시작

# .34


def check():
    _list = input().split(" ")
    for i in range(len(_list)-1):
        if _list[i] > _list[i+1]:
            return "NO"
        else:
            continue
    return "YES"


# .30
def findWord():
    txt = input("문장: ")
    word = input("단어: ")
    print(txt.find(word))

# .29


def upperCase():
    alp = input("알파벳: ")
    return "YES" if alp.isupper() else "NO"


def printUpperCase():
    txt = input("알파벳들: ")
    result = ""
    for i in range(len(txt)):
        if txt[i].isupper():
            result += txt[i]
    return result
# .28


def twoGram():
    _input = input("2-gram:")
    for i in range(len(_input)-1):
        print(_input[i:i+2])

# .27


def mathScore():
    name = input("학생 이름: ").split()
    score = input("수학 점수: ").split()
    math = {}
    for i in range(len(name)):
        math[name[i]] = score[i]
    return math

# .정답은 dict함수와 zip함수 사용


def mathDic():
    names = input().split()
    scores = map(int, input().split())

    result = dict(zip(names, scores))
    print(result)

# 6/3
# 26


def planetInEng():
    K = input("행성: ")
    planet = {
        '수성': "Mercury", '금성': "Venus", '지구': "Earth", '화성': "Mars", '목성': "Jupiter",
        '토성': "Saturn", '천왕성': "Uranus", '해왕성': "Neptune"
    }
    print(planet[K])
# 25


def areaOfCircle():
    r = int(input("정수 반지름: "))
    return r*r*3.14
# 24


def upperCase():
    name = input("참가자: ")
    print(name.upper())

# 35 ???

# 36


def mulTable():
    n = int(input("구구단: "))
    result = ""
    for i in range(1, 10):
        result += str(i * n) + " "
    print(result)

# 6/4
# 37


def election():
    _list = input().split()
    candidates = list(set(_list))
    countList = []
    for cnd in candidates:
        countList.append(_list.count(cnd))
    _index = countList.index(max(countList))
    print("%s(이)가 총 %s표로 반장이 되었습니다." % (candidates[_index], max(countList)))

# 38


def ranking():
    _input = input().split()
    print(set(_input))
    scores = list(set(_input))
    # print(scores)
    rank1 = scores[-1]
    rank2 = scores[-2]
    rank3 = scores[-3]
    # print(rank1, rank2, rank3)
    candy = _input.count(rank1) + _input.count(rank2) + _input.count(rank3)
    print(candy)


# 6/5
# 39

def correct():
    _input = input()
    _input = _input.replace('q', 'e')
    _input = _input.replace('b', 'n')
    return _input


def correct2():
    _input = input()
    print(_input.replace('q', 'e').replace('b', 'n'))

# 40


def weightLimit():
    limit = int(input())
    number = int(input())
    weightList = []
    for i in range(number):
        weightList.append(int(input()))
    for j in range(1, len(weightList)):
        if sum(weightList[:j+1]) > limit:
            return j

# 6/6
# 41


def primeNumber():
    n = int(input("정수를 입력하세요: "))
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return "NO"
    return "YES"


def check_prime(n):
    if n <= 1:
        return "NO"
    i = 2
    소수 = True
    while (i**2) < n:
        if n % i == 0:
            소수 = False
            break
        i += 1
    return "YES" if 소수 else "NO"


# 42


def weekday():
    [a, b] = map(int, input("2020년 _월 _일은 무슨 요일일까요?").split())
    diff = (datetime.date(2020, a, b)-datetime.date(2020, 1, 1)).days
    week = {
        0: "WED", 1: "THU", 2: "FRI", 3: "SAT", 4: "SUN", 5: "MON", 6: "TUE"
    }
    return week.get(diff % 7)

# 43


def binary():
    n = int(input("10진수 숫자를 입력하세요: "))
    result = ""
    while True:
        result += str(n % 2)
        if n // 2 == 0:
            return result[::-1]+"(2)"
        n = n // 2

# 44


def sum():
    _input = input("정수: ")
    sum = 0
    for n in _input:
        sum += int(n)
    return sum


def sum2():
    result = 0
    for i in input():
        result += int(i)
    return result


# 45
t = time.time()
minu = t / 60
hour = minu / 60
day = hour / 24
year = day / 365
# print(1970 + math.floor(year))

# 46


def totalSum():
    oneLine = ""
    sum = 0
    for i in range(1, 101):
        oneLine += str(i)
    # print(oneLine)
    for j in oneLine:
        sum += int(j)
    print(sum)

# 47


def people():
    people = [
        ('이호준', '01050442903'),
        ('이호상', '01051442904'),
        ('이준호', '01050342904'),
        ('이호준', '01050442903'),
        ('이준', '01050412904'),
        ('이호', '01050443904'),
        ('이호준', '01050442903'),
    ]
    peopleSet = set(people)
    numOfPeople = len(peopleSet)
    print(f'중복을 제거한 접수 인원은 {numOfPeople}명 입니다.')

# 48


def case():
    inputSting = input('변환할 문자열: ')
    newString = ""
    for letter in inputSting:
        if isupper(letter):
            newString += letter.lower()
        elif islower(letter):
            newString += letter.upper()
        else:
            return '입력한 값에 오류가 있습니다.'
    return newString

# 49


def maxValue():
    _input = input('10개의 정수를 입력하세요: ')
    inputList = map(int, _input.split())
    return max(inputList)

# 50


def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-2, -1, -1):
            if data[j] > data[j+1]:
                f = data[j]
                b = data[j+1]
                data[j] = b
                data[j+1] = f
    for i in range(n):
        print(data[i], end=" ")


# n = int(input())
# data = list(map(int, input().split()))
# n = len(data)


# if __name__ == "__main__":
#     print(maxValue())

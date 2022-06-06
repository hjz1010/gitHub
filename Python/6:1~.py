# -*- coding: utf-8 -*-

# 6/2 Python100제 시작

# .34
import math


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


if __name__ == "__main__":
    print(check_prime(12))

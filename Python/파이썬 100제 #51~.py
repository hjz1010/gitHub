# -*- coding: utf8 -*-
# 51

import math
from re import L
from this import s
from xml.sax.xmlreader import InputSource


def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while 그룹_하나 and 그룹_둘:
        if 그룹_하나[0] < 그룹_둘[0]:
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값


# 주어진리스트 = input().split()
# 주어진리스트 = list(map(int, 주어진리스트))

# print(병합정렬(주어진리스트))

# 52


def 퀵정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    if 입력리스트의길이 <= 1:
        return 입력리스트
    기준값 = 입력리스트.pop(입력리스트의길이//2)
    그룹_하나 = []
    그룹_둘 = []

    for i in range(입력리스트의길이-1):
        if 입력리스트[i] < 기준값:
            그룹_하나.append(입력리스트[i])
        else:
            그룹_둘.append(입력리스트[i])
    return 퀵정렬(그룹_하나) + [기준값] + 퀵정렬(그룹_둘)


# 주어진리스트 = input().split(' ')
# 주어진리스트 = [int(k) for k in 주어진리스트]

# print(퀵정렬(주어진리스트))

# 53

def bracketCheck():
    inputString = input("괄호문자열: ")
    checkOpen = [
        1 if letter == '{'
        else 2 if letter == '['
        else 3 if letter == '('
        else 0 for letter in inputString]
    checkClose = [
        1 if letter == '}'
        else 2 if letter == ']'
        else 3 if letter == ')'
        else 0 for letter in inputString]
    print(checkOpen, checkClose)
    if checkOpen.count(1) == checkClose.count(1) and checkOpen.count(2) == checkClose.count(2) and checkOpen.count(3) == checkClose.count(3):
        return 'YES'
    else:
        return 'NO'
# 괄호 갯수만 체크하면서 쓸데없이 복잡하게 작성함...
# 저럴꺼면 한문장으로만 끝낼 수 있잖니 if inputString.count('{') == inputString.count('}') and blahblahblah
# 괄호 갯수만 체크하는 것이 아니라 순서가 적절한지도 체크해야함


def bracketCheck2():
    inputString = input("괄호문자열: ")
    for checkPoint in [['{', '}'], ['[', ']'], ['(', ')']]:
        checkList = []
        for letter in inputString:
            if letter == checkPoint[0]:
                checkList.append(letter)
            if letter == checkPoint[1]:
                if checkList == []:
                    return 'NO'
                checkList.pop()
        if checkList != []:
            return 'NO'
    if checkList == []:
        return 'YES'

# 이러면 각 괄호의 순서를 고려하여 판별할 수 있지만, 서로 다른 괄호의 순서가 맞는지는 판별이 안된다. ex. {python(if}) > True


def bracketCheck3():
    inputString = input("괄호문자열: ")
    checkList = []
    checkPoint = [['{', '}'], ['[', ']'], ['(', ')']]
    for letter in inputString:
        if letter == checkPoint[0][0] or letter == checkPoint[1][0] or letter == checkPoint[2][0]:
            checkList.append(letter)
        for i in range(3):
            if letter == checkPoint[i][1]:
                if checkList == []:
                    return 'NO'
                elif checkList[-1] == checkPoint[i][0]:
                    checkList.pop()
                else:
                    return 'NO'
    if checkList == []:
        return 'YES'


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

# for문을 돌리기 전에 각 괄호의 갯수가 짝이 맞는지 먼저 확인하고 안 맞는 경우를 걸러내면 반복 횟수를 줄일 수 있다.
# ↓ 정답지 내용
# def math(e):
#     if e.count('(') != e.count(')'):
#         return False
#     괄호 = []
#     for i in e:
#         if i == '(':
#             괄호.append('(')
#         if i == ')':
#             if len(괄호) == 0:
#                 return False
#             괄호.pop()
#     return True

# n = input()
# if math(n) == True:
# 	print("YES")
# else:
# 	print("NO")

# 54


def consequtive():
    inputList = list(map(int, input("스템프를 제출하세요: ").split(" ")))
    orderedList = list(set(inputList))
    cnsq = list(range(orderedList[0], orderedList[0] + len(orderedList)))
    return "Yes" if orderedList == cnsq else 'No'
# inputList = [int(i) for i in input("스템프를 제출하세요: ").split(" ")]
# orderedList = sorted(inputList)  # 단순 정렬만 할꺼면 sorted가 훨씬 간단


def consequtive2():
    inputList = [int(i) for i in input("스템프를 제출하세요: ").split(" ")]
    orderedList = sorted(inputList)
    cnsq = list(range(orderedList[0], orderedList[0] + len(orderedList)))
    return "Yes" if orderedList == cnsq else 'No'


def stamp():
    inputList = map(int, input("스탬프: ").strip().split())
    inputList = sorted(inputList)
    startNum = inputList[0]
    if inputList == list(range(startNum, startNum+len(inputList))):
        return "YES"
    return "NO"

# 55


원판의이동경로 = []


def 하노이(원반의수, 시작기둥, 목표기둥, 보조기둥):
    # 원판이 한개일 때에는 옮기면 됩니다.
    if 원반의수 == 1:
        원판의이동경로.append([시작기둥, 목표기둥])
        return None
    # 원반의 n-1개를 보조기둥으로 옮기고
    하노이(원반의수-1, 시작기둥, 보조기둥, 목표기둥)
    # 가장 큰 원반은 목표기둥으로
    원판의이동경로.append([시작기둥, 목표기둥])
    # 보조기둥과 시작기둥을 바꿉니다!
    하노이(원반의수-1, 보조기둥, 목표기둥, 시작기둥)

# user_input = int(input())
# 하노이(user_input, 'A', 'C', 'B')
# print(len(원판의이동경로))

# 56


nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England': 242900,
    'a': 10}
# k = nationWidth.pop("korea")
# 변수k에 한국의 면적 할당, 딕셔너리에는 나머지 국가만 남긴다
# def diff(x): return abs(nationWidth[x] - k)
# nation = min(nationWidth, key=diff)
# print(nation, diff(nation))

# #답안.... 별론데....?
# w = nationWidth['korea']
# nationWidth.pop('korea')
# l = list(nationWidth.items())     # 튜플쌍으로 이루어진 리스트
# gap = max(nationWidth.values())   # 면적 중 최대값...을 왜? 그게 왜 gap??
# item = 0

# for i in l:                       # 각 튜플마다 반복문
#     if gap > abs(i[1] - w):       # 면적 차이가 젤 적은 튜플을 찾는 반복문
#         gap = abs(i[1] - w)
#         item = i
# print(item[0], gap)

# 57


def countOne():
    txt = ""
    for i in range(1001):
        txt += str(i)
    return txt.count("1")


# 58
# _input = input("정산: ")
# reverse_input = _input[::-1]
# result = reverse_input[0]
# for i in range(1, len(reverse_input)):
#     if i % 3 == 0:
#         result += "," + reverse_input[i]
#     else:
#         result += reverse_input[i]
# result = result[::-1]
# print(result)

# 재귀함수로 풀어보라구?

# 뒤에서 3개씩 가져와서 콤마와 함께 새 문자열 앞쪽에 넣어보자


# def comma(num):
#     if len(num) <= 3:
#         result = num
#         return result
#     result = comma(num[:-3]) + ',' + num[-3:]
#     return result


# num = input("정산: ")
# print(comma(num))

# 59
# _input = input("가운데 넣을 글자: ")
# print(_input.center(50, "="))

# 60
# student = ['강은지', '김유정', '박현서', '최성훈', '홍유진',
    #    '박지호', '권윤일', '김채리', '한지호', '김진이', '김민호', '강채연']

# sortedStd = sorted(student)
# for i in range(len(sortedStd)):
#     print(f"번호: {i+1}, 이름: {sortedStd[i]}")

# sortedStd = sorted(student)
# for num, std in enumerate(sortedStd, start=1):
#     print(f"번호: {num}, 이름: {std}")

# 61 문자열 압축


def shorten():
    _input = input("문자열: ")
    result = _input[0]
    count = 0
    for txt in _input:
        if txt == result[-1]:
            count += 1
        else:
            result += str(count)
            result += txt
            count = 1
    result += str(count)
    return result

# 62. 20190923 출력


# a = 'aacdddddddddfffffffffgghhh'
# _list = 'abcdefgh'
# for alph in _list:
#     print(a.count(alph), end="")

# 63. 줄여 말하기

# _input = input("긴 문장: ")
# _sep = _input.split(" ")
# print("줄임말..: ", end="")
# for word in _sep:
#     print(word[0], end="")

# 64. 이상한 엘베


def elevator():
    N = int(input("엘베 정량(kg): "))
    # max7kg = math.floor(N/7)
    max3kg = N//3
    for i in range(max3kg + 1):
        if (N - 3 * i) % 7 == 0:
            j = (N - 3 * i) // 7
            return i+j
    return -1


# 65.
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

# result = []

# for i in range(math.ceil(len(a)/2)):
#     result.append([a[2*i], b[2*i]])
#     try:
#         result.append([b[2*i+1], a[2*i+1]])
#     except:
#         pass
# print(result)

# result = []
# count = 0
# for _set in zip(a, b):
#     _list = list(_set)
#     if count % 2 == 0:
#         result.append(_list)
#     else:
#         reverse_list = _list[::-1]
#         result.append(reverse_list)
#     count += 1
# print(result)

# 66 블럭탑 쌓기

탑s = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
규칙 = "ABD"

# result = []
# for 탑 in 탑s:
#     인덱스 = None
#     for i in range(len(탑)):
#         if 탑[i] in 규칙:
#             try:
#                 if 인덱스 > 규칙.index(탑[i]):
#                     result.append(탑 + ": 불가능")
#                     break
#                 else:
#                     인덱스 = 규칙.index(탑[i])
#             except:
#                 인덱스 = 규칙.index(탑[i])
#         if i == len(탑)-1:
#             result.append(탑 + ": 가능")
# print(result)

# 결과 = []
# for 탑 in 탑s:
#     비교할블럭 = ""
#     for 블럭 in 탑:
#         if 블럭 in 규칙:
#             비교할블럭 += 블럭
#     수정규칙 = 규칙
#     for 블럭 in 규칙:
#         if 블럭 not in 비교할블럭:
#             수정규칙 = 수정규칙.replace(블럭, "")

#     결과.append("가능" if 비교할블럭 == 수정규칙 else "불가능")
# print(결과)

# 결과 = []
# for 탑 in 탑s:
#     비교할블럭 = ""
#     for 블럭 in 탑:
#         if 블럭 in 규칙:
#             비교할블럭 += 블럭
#     수정규칙 = "".join(블럭 for 블럭 in 규칙 if 블럭 in 비교할블럭)
#     결과.append("가능" if 비교할블럭 == 수정규칙 else "불가능")
# print(결과)

# 67 민규의 악수
# 진행된 총 악수 n번
# 민규만 중간에 퇴장
# = > 민규의 악수 횟수(m), 행사 참가자 수(N)

# N명이 전부 악수를 한다면 총 악수 횟수는
# (N-1)+(N-2)+...+2+1 = (N-1) * N / 2
# 민규가 빠지면, 전체 인원은 - 1, (N-2)*(N-1) / 2 + m
# 여기서, m은 N보다 작다

n = int(input("총 악수 횟수: "))
N = 2
while True:
    if (N-2)*(N-1) / 2 <= n and n < (N-1)*N / 2:
        break
    N += 1
m = 1
while True:
    if (N-2)*(N-1) / 2 + m == n:
        break
    m += 1
print([m, N])

# if __name__ == "__main__":
#     print(elevator())

# -*- coding: utf8 -*-
# 51

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


if __name__ == "__main__":
    print(consequtive2())

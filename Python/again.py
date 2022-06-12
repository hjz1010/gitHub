# -*- coding: utf8 -*-
# 파이썬 100제 35번

def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two


a = one(2)
b = one(3)
c = one(4)
print(a(10))   # 중첩함수는 이렇게 선언하고 호출하는구나 익숙해지자
print(b(10))
print(c(10))


# 파이썬 100제 37번

data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

# max함수에 key값을 따로 지정할 수 있다..!!
print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')

# 파이썬 100제 44번


def mySum():
    _input = input("정수: ")
    sum = 0
    for n in _input:
        sum += int(n)
    return sum


def AnsSum():
    result = 0
    for i in input():  # input을 바로 반복문 안에 코딩하면 깔끔하네!!
        result += int(i)
    return result


# 파이썬 100제 48번
a = input()
b = []

for i in a:
    if i.islower():
        b.append(i.upper())
    else:
        b.append(i.lower())

for i in b:
    print(i, end='')  # 문자열을 출력하는 다양한 방법!

# 파이썬 100제 49번
data = list(map(int, input().split()))
print(sorted(data)[-1])  # max값을 구하기 위해 숫자를 정렬!!

# 파이썬 100제 50번


def bubble():
    data = list(map(int, input().split()))
    n = len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                # 값을 바꿔 넣을땐 set을 이용!
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")


# 파이썬 100제 51번 - merge sort

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


주어진리스트 = input().split()
주어진리스트 = list(map(int, 주어진리스트))

print(병합정렬(주어진리스트))


# 파이썬 100제 52번 - quick sort

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


주어진리스트 = input().split(' ')
주어진리스트 = [int(k) for k in 주어진리스트]

print(퀵정렬(주어진리스트))


# 53 - 정답지

def math(e):
    if e.count('(') != e.count(')'):
        return False
    괄호 = []
    for i in e:
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:
                return False
            괄호.pop()
    return True


n = input()
if math(n) == True:
    print("YES")
else:
    print("NO")

# 53 나의 최종 수정안


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

# 54


user_input = input().split(' ')
user_input = [int(i) for i in user_input]


def sol(l):
    l = sorted(l)
    for i in range(len(l) - 1):
        if l[i]+1 != l[i+1]:
            return 'NO'
    return 'YES'


print(sol(user_input))

# 나는
#   #cnsq = list(range(orderedList[0], orderedList[0] + len(orderedList)))
#   # return "Yes" if orderedList == cnsq else 'No'

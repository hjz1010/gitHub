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
            print(data[i], end= " ")

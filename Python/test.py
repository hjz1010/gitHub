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
주어진리스트 = [int(i) for i in 주어진리스트]

print(퀵정렬(주어진리스트))

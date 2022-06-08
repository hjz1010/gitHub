# mel = {'name': 'HHJ', 'age': 33, 'job': 'programmer'}

# mel.update({'birth': '1988.10.10'})


# data = {}

# # key로 'a'를 추가학 value 0을 설정함, setdefault는 현재 value 값을 리턴
# ret = data.setdefault('a', 0)
# # print(ret, data)

# ret = data.setdefault('a', 1)   # 이미 key가 있는 경우 setdefault 현재 value 값을 리턴
# print(ret, data)

name = ['Mel', 'Jay', 'Ahkim']
age = [33, 30, 32]
# print(zip(name, age))
a = dict(zip(name, age))
# print(a)

b = {k: v+30 for k, v in zip(a.keys(), a.values())}
print(b)

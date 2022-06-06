#파이썬 100제 35번

def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))


#파이썬 100제 37번

data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')

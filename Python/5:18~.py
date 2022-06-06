'''
#5/18

import random
def tanos(list):
    random.shuffle(list)
    a = int(len(list)*1/2)
    if len(list) % 2 == 1 :
        a = random.choice([a, a+1])
    print(list[:a])
        
list = [2, 3, 1, 6 ,5, 7]

if __name__ == '__main__':
    tanos(list)


import random
def pi(n):
    total = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if (x*x)+(y*y) <= 1 :
            total += 1
    p = total / n
    pi = p * 4
    print("π: " + str(pi))

#5/19

with open('temp.txt', 'r') as f:
    text = f.read()

def countLetter(txt):
    print("글자수:", len(txt),"자")

def countWord(txt):
    print("단어 수:", txt.count(" ")+1, "자")
    
if __name__ == '__main__':
    countLetter(text)
    countWord(text)


#5/20
value = input("값을 입력하세요: ")
result = ""
for i in range(len(value)):
    if i % 2 == 1 and value[i].isdigit():
            result += "*"
    else:
        result += value[i]

print(result)


#5/21
def josephus():
    _input = input("병사의 수와 간격 적어주세요. \n ex. 10 3 \n")
    n = int(_input.split(" ")[0])
    k = int(_input.split(" ")[1])
    _list = list(range(1,n+1))  
    newList =[]
    i = 0
    while True :
        try:
            _list[i]
            if (i+1) % k != 0 :
                newList.append(_list[i])
            i += 1
        except IndexError:
            if len(newList) == 1:
                return newList[0]
            _list = _list + newList
            newList = []
if __name__ == "__main__":
    print(josephus())
    

def fun(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    result = len(str(fac))-len(str(fac).strip("0"))
    return result
    
if __name__ == "__main__":
    print(fun(int(input())))

    
result = 0
for n in range(2,1001):
    count = 0
    for i in range(2,n):
        if n % i == 0:
            break
        else:
            count += 1
    if count == n-2:
         result += 1
print(result)


def strip(txt):
    return txt.strip("\n")
def replace(txt):
    return txt.replace("-","")

with open('numbers.txt', 'r') as f:
    numbers_1 = f.readlines()
    numbers_2 = list(map(strip,numbers_1))   # \n 제거
    numbers_3 = numbers_2[1:]                # 첫줄 제거
    numbers = list(map(replace,numbers_3))   # 하이픈(-)제거
   
two = ["A", "B", "C"]
three = ["D", "E","F"]
four = ["G","H","I"]
five = ["J","K","L"]
six = ["M","N","O"]
seven = ["P","R","S"]
eight = ["T","U","V"]
nine = ["W","X","Y"]
_list = two + three + four + five + six + seven + eight + nine

for i in range(len(numbers)):
    for j in range(len(_list)):
        letter = _list[j]
        numbers[i] = numbers[i].replace(letter, str(j//3 +2))
numbers.sort()           # 오름차순 정렬
count = 1
dup = 0
for k in range(len(numbers)-1):
    if numbers[k] == numbers[k+1]:
        count += 1
        result = numbers[k][:3] + "-" + numbers[k][3:]
        dup += 1 
    elif count > 1 :
        print(result, count)
        count = 1       
if dup == 0:
    print("No dupliates")
'''


'''
#5/4
for a in range(1,334):
    for b in range(a,500):
        if (a**2) + (b**2) == (1000-a-b)**2:
            print("a = %d, b = %d, c = %d" %(a,b,1000-a-b))
            print("그러므로 a x b x c = %d" %(a*b*(1000-a-b)))


sumOfSqr = 0
_sum = 0
sqrOfSum = 0

for n in range(1,101):
    sumOfSqr += n**2
    _sum += n 
    
sqrOfSum = _sum**2
result = sqrOfSum - sumOfSqr
print(result)


print(abs(sum(range(1,101))**2 - sum(x**2 for x in range(1,101)))) 


word = input("암호화할 문장을 입력하세요: ")
n = int(input("자연수를 입력하세요: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
newWord = ""
for i in word:
    index = alphabet.index(i)
    while index+n > 52:
        index = index - 52
    newWord += alphabet[index+n]
print(newWord)


def cipher():
    word, n = input("암호화할 문장, 숫자를 입력하세요: ").split(",")
    n = int(n)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet += alphabet.upper()
    newWord = ""
    for i in word:
        try:
            index = alphabet.index(i)
            while index+n > 52:
                index = index - 52
            newWord += alphabet[index+n]
        except:
            newWord += i 
    print(newWord)
'''
'''
#5/5
def binary(n):
    bin = 0
    i = 0
    m = int(n)
    while n > 2 ** i:
        bin += (m%2) * (10**i)
        m = m//2
        i += 1
    print(bin)

for n in range(999,99,-1):
    for m in range(999,n-1,-1):
        num = str(n*m)
        if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
            print("%d (= %d x %d)"%(n*m,n,m))
            break
    if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
        break
'''
'''
# 5/6
def answer(a,b,c):
    if a == 0 :
        x = int(- c/b)
    elif b**2 - 4*a*c < 0:
        x = "해가 없다."
    elif b**2 - 4*a*c == 0:
        x = int(-b / (2*a))
    else:
        x = list(map(int,[(-b+(b**2 - 4*a*c)**(1/2))/(2*a) ,(-b-(b**2 - 4*a*c)**(1/2))/(2*a)] ))
    print(x)    

number = 20
result = 0 
while result == False:
    number += 1
    for i in range(1,21):
        if number % i != 0:
            break
    if i == 20 :
        result = number
print(result)
        
def mid(a,b,c):
    _list = [a,b,c]
    _list.sort()
    result = _list[1]
    print(result)

def length(n):
    print(len(str(n)))

def count():
    sentence = input("글자수 세기\n")
    new = sentence.replace("\n", "")
    new2 = new.replace(" ", "")
    print("글자수: %d"%(len(new2)))


def aaa(_list):
    newL&ist= []
    result = []
    for i in range(len(_list)):
        newList = _list[:i] + _list[i+1:]
        mul = 1
        for j in range(len(newList)):
            mul *= newList[j]
        result.append(mul)    
    print(result)
_list = input("숫자를 입력하세요: ")
aaa(list(map(int,_list.split(","))))
    
'''
'''
#5/7
chr = input("문자를 입력하세요: ")
print("%s는 아스키코드로 %d입니다."%(chr,ord(chr)))

number = ""
for i in input():
    try:
        int(i)
        number += i
    except:
        continue
print(number)

print("%d의 자릿수"%10**(len(input())-1))

_list= list(map(int,input("리스트를 입력하세요: ").strip("[]").split(",")))
even, odd = 0, 0
for num in _list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("홀수 %d개, 짝수 %d개" %(odd, even))

def count(lst):
    odd = len([x for x in lst if x % 2 == 1 ])
    print("홀수 %d개, 짝수 %d개" %(odd, len(lst)-odd))

def cck(a,b,c):
    if a+b+c != 180:
        return "삼각형이 아니다."
    elif a < 90 and b < 90 and c < 90:
        return "예각 삼각형"
    elif a ==90 or b == 90 or c == 90:
        return "직각 삼각형"
    elif a > 90 or b > 90 or c > 90 :
        return "둔각 삼각형"

print(sum(int(x) for x in input("양의 정수: ")))
'''
'''
#5/8
import datetime

def remain():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    home = datetime.datetime.strptime(date+" 17:30:00","%Y-%m-%d %H:%M:%S")
    remain = home - now
    if remain.days < 0 :
        print("퇴근하세요!")
    else:
        scd = remain.seconds
        h = scd // 3600
        m = (scd % 3600) //60
        s = (scd % 3600) % 60
        print("퇴근까지 남은 시간은 %s:%s:%s입니다."%(h,m,s))

word = input()
str = ""
int = ""
for i in word:
    if i.isdigit():
        int += i
    else:
        str += i
print("str : %s \nint : %s"%(str,int))

word = input()
print("str: " + "".join([i for i in word if not i.isdigit()])
      +"\n"
      +"int: " + "".join([i for i in word if i.isdigit()]))

def multiple(x,n):
    try:
        x.isdigit()
        if int(x) % int(n) == 0 :
            print("%s는 %s의 배수 입니다."%(x,n))
        else:
            print("%s는 %s의 배수가 아니다."%(x,n))
    except:
        print("정수를 입력해주세요!")
x, n = input("두개의 정수를 입력해주세요.(ex. 12,5) :").split(",")
multiple(x,n)

multiple = lambda x, n : x in range(0,x+1,n)

diagonal = lambda x,y: (x*x + y*y)**(1/2)

x = input()
try:
    x = float(x)
    print("정수" if x % 1 == 0 else "소수")
    if x % 1 == 0:
        print("정수")
    else:
        print("소수")
except:
    print("math error")

def marathon():
    r = float(input("100m 몇 초?"))
    t = r * 421.95
    h, t = divmod(t, 3600)
    m, s = divmod(t, 60)
    print("마라톤 기록: %d시간 %d분 %d초"%(h,m,s))

if __name__ == '__main__':
    marathon()

password = lambda num: print(int(int((num**0.5)*1000)-num))
  
if __name__ == '__main__':
    password(int(input("암호화할 숫자를 입력하세요: ")))

import random
x = random.randrange(1,101)
count = 1
while True:
    _input = int(input("1~100 숫자 입력: "))
    if _input > x :
        print("DOWN")
        count += 1
    elif _input < x :
        print("UP")
        count += 1
    else:
        print("정답입니다! %d회 만에 맞췄어요."%count)
        break
    
'''
'''
# 5/9
# d(324) = 3 + 2 + 4 + 324
dList = []
for n in range(1, 5000):
    if n // 10  == 0 :
        d = n + n
    elif n // 100 == 0 :
        d = (n//10) + (n%10) + n
    elif n // 1000 == 0 :
        d = (n//100) + ((n%100)//10) + (n%10) + n
    else :
        d = (n//1000) + ((n%1000)//100) + ((n%100)//10) + (n%10) + n
    dList.append(d)
total = 0
for self in range(1,5000):
    if self not in dList:
        total += self
print(total)


dList = []
for n in range(1, 5000):
    d = n
    for i in range(0,4):
        d += (n%(10**(i+1)))//(10**i)
    dList.append(d)
total = 0
for self in range(1,5000):
    if self not in dList:
        total += self
print(total)

print(sum([s for s in range(1,5000) if s not in
           [(sum([(n%(10**(i+1)))//(10**i) for i in range(0,4)])+n) for n in range(1,5000)]]))
'''
'''
#5/10
count = 0
for num in range(1,10000):
    for i in str(num):
        if i == '8' :
            count += 1
print(count)

print(len([i for i in str(list(range(1,aa10001))) if i == '8']))

arr = list(input("배열을 입력해주세요: ").split(" "))
print(" ".join([str(x) for x in arr if int(x) < 0] + [str(y) for y in arr if int(y) > 0]))

'''
'''
#5/11
s = list(map(int,input("점들을 입력하세요. ex)1,3,4,8,13,17,20 \n :").split(",")))
dict = {}
for (x,y) in zip(s[:-1],s[1:]):
    dict[y-x] = (x,y)
print(dict[min(dict.keys())])
'''
def spair(S):
    dict = {}
    for (x, y) in zip(S[:-1], S[1:]):
        if not dict.get(y-x):
            dict[y-x] = [(x,y)]
        else:
            dict[y-x] = dict[y-x] + [(x,y)]

    return dict[min(dict.keys())]
#S = [1, 3, 4, 8, 13, 17, 20] 
S = [1,2,4,5,8,15,19]
print(spair(S))

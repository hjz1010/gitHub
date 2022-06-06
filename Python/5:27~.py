#5/27
'''
_input = input().split(" ")
n = int(_input[0])
_list = _input[1:]
new_list = _list[(-1*n):] + _list[:(-1*n)]
print(" ".join(new_list))


import datetime
_input = input("")
result = 0
with open('timelog.txt','r') as timelog:
       for time in timelog:
           time_list = time.strip('\n').split(" ")
           time1 = datetime.datetime.strptime(time_list[0],'%H:%M:%S').timestamp()
           time2 = datetime.datetime.strptime(time_list[1],'%H:%M:%S').timestamp()
           input_time = datetime.datetime.strptime(_input,'%H:%M:%S').timestamp()

           if time1 - input_time < 0 and input_time - time2 < 0:
               result += 1
print("%s명이 사무실에 있습니다." %result)

_input = input("")
result = 0
with open('timelog.txt','r') as timelog:
       for time in timelog:
           time_list = time.strip('\n').split(" ")
           time1 = "".join(time_list[0].split(":"))
           time2 = "".join(time_list[1].split(":"))
           input_time = "".join(_input.split(":"))

           if time1 < input_time and input_time < time2:
               result += 1
print("%s명이 사무실에 있습니다." %result)


#5/29

def Mabu():
    result = ''
    while 1:
        input_num = int(input())
        if input_num == 0: break
        else:
            count = 0
            status = False
            for i in range(1,input_num +1):
                if input_num % i == 0 : status = not status
            result += (lambda x: 'yes' if x else 'no')(status)  + '\n'   
    return result


def min_num(num):
    target = 0
    for i in range(100):
        target += 10**i
        if target % num == 0:
            return i+1
    return '알맞은 숫자를 입력하세요.'

def min_num2(num, i=0, target=0):
    while 1:
        target += 10**i
        if target % num == 0:
            return i+1
        i += 1

def min_num3(num):
    target = '1'
    while 1:
        if int(target) % num == 0 : return len(target)
        else : target += '1'


#5/30

with open('triangel.txt','r') as textfile:
    for line in textfile:
        legs = line.strip('\n').split(" ")
        a, b, c = map(float, legs)
        r = "헤론의 공식으로 구한다.."
        print('The radius of the round table is: ' + round(r, 3))
'''

#5/31

def sort_program(_list):
    for i in range(1,len(_list)):
        black = _list[i]
        for j in range(i,0,-1):
            gray = _list[j-1]
            if gray > black : (_list[j-1], _list[j]) = (_list[j], _list[j-1])
            else : break
    print(_list)

def sort_program2(_list):
    for i in range(1,len(_list)):
        black = _list[i]
        for j in range(i,0,-1):
            gray = _list[j-1]
            if gray > black : new_position = j-1
            else:
                new_position = j
                break
        _list[new_position+1:i+1] = _list[new_position:i]
        _list[new_position] = black
    print(_list)
    

if __name__ == "__main__":    
    sort_program2([5,2,4,6,1,3])


#5/23

_list  = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
def change():
    k, n = set(input("변환할 정수와 원하는 진법을 적어주세요. \n ex. 233, 2 \n :").split(","))
    k = int(k); n = int(n);
    result = ""
    if n < 10 :
        while True :
            result += str(k % n )
            k = k // n
            if k == 0 :
                return (result[::-1]) + "(%d)" %n
    else:
        while True:
             result += str(k%n) if (k%n)<10   else _list[k%n]
             k = k // n
             if k == 0 :
                return (result[::-1]) + "(%d)" %n
           
    while True :
        if n < 10 :
            result += str(k % n )
        else:
            result += str(k%n) if (k%n)<10   else _list[k%n]
        k = k // n            
        if k == 0 :
            return (result[::-1]) + "(%d)" %n
            k = k // n

if __name__== "__main__":
    print(change())


rule = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F",
        "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L",
        "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R",
        "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X",
        "-.--":"Y", "--..":"Z", "":" "
        }
sign = input("모스부호: ").split(" ")
result = ""
for word in sign:
    result += rule[word]
print(result)


#5/26

word = input("변환할 camelCase를 입력해주세요: ")
for letter in word:
    if letter.isupper(): word = word.replace(letter,"_"+letter.lower())
    elif letter.isdigit(): word = word.replace(letter,"_"+letter)
print(word)


_input = input("변환할 camelCase를 입력해주세요: ")
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print("".join("_"+l.lower() if l in a else l for l in _input))

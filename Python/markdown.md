## 51번. merge sort를 만들어보자
[그래서 merge sort가 뭔데!](https://gmlwjd9405.github.io/images/algorithm-merge-sort/merge-sort-concepts.png)
```python
def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while (그룹_하나) and (그룹_둘) :
        if (그룹_하나[0] < 그룹_둘[0]):
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값

#주어진리스트 = [180, 145, 165, 45, 170, 175, 173, 171]
#빈칸을 채워주세요

주어진리스트 = input().split(' ')
주어진리스트 = [int(i) for i in 주어진리스트]

print(병합정렬(주어진리스트))
```
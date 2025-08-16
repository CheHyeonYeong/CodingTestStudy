# 파이썬 알고리즘 문제풀이 입문 강의 1장

> 💡 스터디 시작 전 **파이썬 설치(Python3)** 를 완료해주세요!

## 1.  반복문을 이용한 문제 풀이

**예제 문제**

1.  1부터 N까지 홀수 출력하기
2.  1부터 N까지의 합 구하기
3.  N의 약수 출력하기

📌 input() → 문자열 입력을 받고 int()로 숫자로 변환해야 함

```
n = int(input("숫자를 입력하세요: "))

# 1부터 n까지 출력
for i in range(1, n+1):   # n 포함하려면 n+1
    print(i)
```

**홀수만 출력하기**

---

## 2.  문자열과 내장 함수

-   **대문자** : msg.upper()
-   **소문자** : msg.lower()
-   **찾기** : msg.find('a') → 제일 처음 만난 위치 (없으면 -1)
-   **개수 세기** : msg.count('a')
-   **슬라이스** : msg\[:2\] (0번 ~ 1번까지만 출력)
-   **길이** : len(msg)

**문자열 접근**

```
msg = "Hello"
for i in range(len(msg)):
    print(msg[i], end=" ")

for x in msg:
    print(x, end=" ")
```

**대소문자/알파벳 판별**

-   isupper(), islower(), isalpha()

**아스키 코드**

```
print(ord('A'))   # 65
print(chr(65))    # A
```

---

## 3\. 리스트와 내장 함수

-   빈 리스트 : a = \[\] 또는 a = list()
-   추가 : a.append(값)
-   삽입 : a.insert(인덱스, 값)
-   삭제 : a.pop() / a.pop(인덱스) / a.remove(값)
-   합치기 : c = a + b
-   정렬 : a.sort() / a.sort(reverse=True)
-   비우기 : a.clear()

📌 **슬라이스** : a\[:3\] → 인덱스 0,1,2 출력  
📌 **길이** : len(a)

**인덱스와 값 함께 출력**

```
for idx, value in enumerate(a):
    print(idx, value)
```

**조건 체크**

```
if all(x < 60 for x in a):
    print("모두 60 미만")
    
if any(x < 60 for x in a):
    print("하나라도 60 미만")
```

---

## 4\. 2차원 리스트

```
a = [[0]*3 for _ in range(3)]
print(a)
# [[0,0,0],[0,0,0],[0,0,0]]
```

-   행 → 열 순으로 탐색
-   알고리즘 문제에서 표(행렬)로 생각하면 좋음

---

## 5\. 함수 만들기

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

---

## 6\. 람다 함수 (익명 함수)

```
# 일반 함수
def plus_one(x):
    return x + 1

print(plus_one(1))

# 람다식
plus_two = lambda x: x+2
print(plus_two(2))
```

📌 **map과 함께 쓰면 유용**

```
a = [1,2,3]

print(list(map(plus_one, a)))         # [2,3,4]
print(list(map(lambda x: x+1, a)))    # [2,3,4]
```

✅ 마지막으로 강조할 부분 → **Python은 들여쓰기(indentation)가 문법이다!**  
(중괄호 {} 없음, 들여쓰기 잘못하면 바로 에러 🔥)
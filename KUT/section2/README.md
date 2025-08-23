from django.db.models.functions import Reverse

# 파이썬 알고리즘 문제풀이 입문 강의 3장


### 1. K번째 약수

- 자연수 N과 K가 주어질 때, N의 약수들 중 K번째로 작은 수를 출력하시오.
- K번째 약수가 없으면 -1을 출력한다.

```python
n,k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%0 == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else: # python은 for-else라는 구문이 있다
    print(-1)
```

### 2. K번째 수

- N개의 숫자열이 주어질 때, s번째부터 e번째까지의 수를 오름차순 정렬한다.
- 정렬된 수 중 k번째 수를 출력하시오.
- 여러 테스트 케이스가 주어진다.

```python
T = int(input())
for t in range(T):
    n, s,e,k = map(int, input().split())
    a = list(map(int,input().split())) # list  시킴
    b = a[s-1:e] # 인덱스번호는 ~~번째보다 -1만큼 있다
    b.sort() # 오름차순 정렬
    print(b[k-1])
```

### 3. K번째 큰 수

- 1~100 사이의 자연수가 적힌 카드 N장이 주어진다.
- 서로 다른 카드 3장을 뽑아 합한 값을 모두 기록했을 때, K번째로 큰 수를 출력하시오.

```python

n,k = map(int, input().split())
a = list(map(int,input().split())) # list  시킴

res = set() # 중복을 제거한다
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i], a[j], a[m])

res = list(res)
res.sort(Reverse=True) # 내림차순으로 정렬
print(res[k-1])
```

### 최솟값 구하기
```python
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf')

for i in range(len(arr)):
    if arr[i] < arrMin: 
        arrMin = arr[i]
```

### 4. 대표값

- N명의 수학 점수가 주어진다.
- 평균(소수 첫째 자리 반올림)을 구한다.
- 평균에 가장 가까운 점수를 가진 학생 번호를 출력한다.
    - 가까운 점수가 여러 개면 점수가 높은 학생, 그래도 여러 명이면 번호가 작은 학생을 선택한다.


```python
n,k = map(int, input().split())
a = list(map(int,input().split())) # list  시킴
min = 2147000000
ave = round(sum(a)/n)

for idx,x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1 
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
```

### 5. 정다면체

- 정 N면체, 정 M면체 주사위를 각각 1개씩 던진다.
- 두 주사위 눈의 합 중 가장 나올 확률이 높은 값을 출력하시오.
- 답이 여러 개면 오름차순으로 모두 출력한다.

```python
n,m = map(int, input().split())
cnt = [0]*(n+m+3) # 눈의 개수의 합만큼 list가 생긴다
max = 0

for i in range(1,n+1):
    for j in range(1, n+1): # 주사위가 던져지는 것은 중복 허용
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i]>max:
        cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
```


### 6. 자릿수의 합

- N개의 자연수가 주어진다.
- 각 자연수의 자릿수 합을 구한다.
- 자릿수 합이 최대인 자연수를 출력한다. (여러 개면 먼저 나온 수 출력)


```python
n = map(int, input().split())
a = list(map(int,input().split())) # list  시킴

def digit_sum(x):
    sum=0
    while x>0:
        sum+= x%10
        x = x//10
    return sum;
max=0;
for x in a :
    tot = digit_sum(x)
    if tot >max:
        max = tot
        res = x
print(res)
```
- 좀 더 쉬운 방법
```python

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

```

### 7. 소수 (에라토스테네스 체)

- 자연수 N이 주어질 때, 1부터 N까지의 소수 개수를 출력하시오.
```python

n = int(input())
ch = [0]*(n+1)
cnt =0

for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1

print(cnt)
```


### 8. 뒤집은 소수

- N개의 자연수가 주어진다.
- 각 수를 뒤집어 정수로 만든 뒤, 그 수가 소수이면 출력하시오.
- 출력 순서는 입력 순서를 따른다.

```python
n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x %i ==0:
            return False
    else:
        return True
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
```


### 9. 주사위 게임

- 세 개의 주사위를 던져 규칙에 따라 상금을 계산한다.
    1. 같은 눈 3개: `10,000 + (같은 눈)*1,000`
    2. 같은 눈 2개: `1,000 + (같은 눈)*100`
    3. 모두 다른 눈: `(가장 큰 눈)*100`
- N명이 게임에 참여했을 때, 가장 많은 상금을 출력한다.

```python
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    elif b==c:
        money = 1000 + (b*100)
    else : 
        money = c * 100
    if money > res :
        res = money
print(res)
```



### 10. 점수 계산 (OX 문제)

- OX 시험 결과가 주어진다.
- 연속으로 맞히면 가산점을 준다.
    - 첫 정답은 1점, 연속되면 2점, 3점 … 으로 증가
- 총 점수를 계산하여 출력한다.


```python
n = int(input())
a = list(map(int, input().split()))
sum =0
cnt =0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt = 0
print(sum)
```




a = input().strip()
b = input().strip()
c = input().strip()
answer = 0
stack = ["Fizz", "Buzz", "FizzBuzz"]

if a not in stack:
    answer = int(a)+3
elif b not in stack:
    answer = int(b)+2
elif c not in stack:
    answer = int(c)+1

if answer %3 ==0 and answer % 5 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)
print('Task 1')

num: int = int(input())
if num >= 0:
    print(num + 1)
else:
    print(num)


print('Task 2')

num_1: int = int(input())
num_2: int = int(input())
num_3: int = int(input())
count = 0
if num_1 > 0:
    count += 1
if num_2 > 0:
    count += 1
if num_3 > 0:
    count += 1
print(count)


print('Task 3')

year: int = int(input())
if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    days = 366
else:
    days = 365
print(days)


print('Task 4')

A: int = int(input())
B: int = int(input())
if A > B:
    A, B = B, A
summa = (A + B) * (B - A + 1) // 2
print(summa)


print('Task 5')

sum_neg: int = 0
prod_poss: int = 1
amount_neg: int = 0
has_positive = False

for i in range(10):
    dig: int = int(input())
    if dig > 0:
        prod_poss *= dig
        has_positive = True
    elif dig < 0:
        sum_neg += dig
        amount_neg += 1

if not has_positive:
    prod_poss = 0

print(sum_neg)
print(prod_poss)
print(amount_neg)



print('Task 6')

n: int = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
print(n, "=", result)



print('Task 7')

s1: float = float(input())
s2: float = float(input())
years = 0
while s1 >= 0.1 * s2:
    s1 *= 2
    s2 *= 3
    years += 1
print(years)



print('Task 8')

n: int = int(input())
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    s = 0
    
    while n > 0:
        digit = n % 10
        s += digit ** 2
        n //= 10
    n = s
if n == 1:
    print(True)
else:
    print(False)


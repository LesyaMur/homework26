import random

print('Task 1')

a: float = -1.6
b: float = 2.99
print(int(a))
print(int(b))


print('Task 2')

s: str = "www.my_site.com#about"
s = s.replace("#", "/")
print(s)


print('Task 3')

a: str = "stroka"
a += "ing"
print(a)


print('Task 4')

s: str = "Ivan Ivanov"
first, last = s.split()
result = f"{last} {first}"
print(result)


print('Task 5')

text: str = "   Hello, Python!   "
new_text = text.strip()
print(new_text)  


print('Task 6')

school_dict = {str(i): random.randint(10,20) for i in range(1,12)}
print(school_dict)   


print('Task 7')

a = ['Hello', 23, 12,4,'summer']
b = a[1]
print(b)


print('Task 8')

str1: str = "employ"
str2: str = "employment"
if str1 in str2:
    print(f'"{str1}" содержится в "{str2}"')
else:
    print(f'"{str1}" не содержится в "{str2}"')



print('Task 9')

x: str = 'My name is Agent Smith'
print(x[1])
print(x[3:16:3])


print('Task 10')

a = [1, 5, 2, 9, 2, 9, 1]
for item in a:
    if a.count(item) == 1:
        print(item)
        break 
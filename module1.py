print("Hello world")

a = 0
b = 0
c = 0
d = 0
a = int(input("Введите значение для a: "))
b = int(input("Введите значение для b: "))
c = int(input("Введите значение для c: "))
d = int(input("Введите значение для d: "))
#print(a, b, c, d)

print('', end='  ')
for i in range(c, d + 1):
    print(i, end="\t")
print()

r = int(0)

for i in range(a, b + 1):
    r = 1
    for j in range(c, d + 1):
        if (r == 1):
            print(i, end=' ')
        r = 0
        print(i * j, end='\t')
    print()

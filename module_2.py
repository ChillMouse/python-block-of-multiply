#!/usr/bin/env python3

while 1:
    a = int(input("Введите целое число: "))
    if (a < 10):
        continue
    elif a > 100:
        break
    else:
        print(a)
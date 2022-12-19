#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = input("Введите строку: ").lower()
    vowels = set("aeiouy")
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print('Количество глассных в предложении = ', count)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = input('Введите строку ')
    s1 = set(a.replace(' ', ''))
    a = input('Введите строку ')
    s2 = set(a.replace(' ', ''))
    print('Общие символы = ', s1.intersection(s2))
    print('Количесвто общих символов = ', len(s1.intersection(s2)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = [1.2, 7.2, 4.6, -1.2, 8.2, 7.8, 3.4, 6.7]
    b = max(a)
    k = b - (b * 0.2)
    new_a1 = [i for i in a if not k <= i <= b]
    new_a2 = [i for i in a if k <= i < b]
    new_a = new_a2 + new_a1
    print(new_a)

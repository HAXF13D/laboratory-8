#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Variant 25

import sys
from random import randint


if __name__ == '__main__':
    A = tuple(randint(0, 100) for i in range(10))
    B = tuple(x * 2 if x % 2 == 0 else x for x in A)
    print(A)
    print(B)

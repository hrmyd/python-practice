#!/bin/python3

"""
practice with stacks 

https://www.hackerrank.com/challenges/balanced-brackets
"""

import sys

opening = '{(['
closing = '})]'

def matched(bracket):
    opening = None
    if bracket == ')':
        opening = '('
    elif bracket == '}':
        opening = '{'
    else:
        opening = '['
        
    return opening
        
t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    new = []
    for b in s:
        if b in opening:
            new.append(b)
        elif b in closing:
            n = matched(b)
            if new and n == new[-1]:
                new.pop()
    
    if len(new) == 0:
        print('YES')
    else:
        print('NO')
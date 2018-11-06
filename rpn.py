#!/usr/bin/env python3

import operator
import colored
import readline
import sys
from termcolor import colored
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()

            text = colored(token, 'blue')
            arg2text = colored(arg2, 'white')
            arg1text = colored(arg1, 'white')
            if arg2 < 0:
                arg2text = colored(arg2, 'red')
            if arg1 < 0:
                arg1text = colored(arg1, 'red')
            result = function(arg1, arg2)
            stack.append(result)
            print(arg2text, text , arg1text, "=")
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

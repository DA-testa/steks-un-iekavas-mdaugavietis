# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            prev = opening_brackets_stack[len(opening_brackets_stack)-1]
            if ((prev.char == '(' and next == ')') or
                (prev.char == '[' and next == ']') or
                (prev.char == '{' and next == '}')
               ):
                opening_brackets_stack.pop()
            else:
                return i+1
    if len(opening_brackets_stack) > 0:
        return len(opening_brackets_stack)
    else:
        return -1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()

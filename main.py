# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def find_mismatch(text):
    opening_brackets_stack = []
    brackets = 0
    for i, next in enumerate(text):
        if next in "([{":
            head = Bracket(next, i+1)
            opening_brackets_stack.append(head)
            brackets += 1

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            if ((head.char == '(' and next == ')') or
                (head.char == '[' and next == ']') or
                (head.char == '{' and next == '}')
               ):
                opening_brackets_stack.pop()
            else:
                return i+1
            brackets -= 1
            if brackets > 0:
                head = opening_brackets_stack[len(opening_brackets_stack)-1]
    if brackets > 0:
        return brackets 
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

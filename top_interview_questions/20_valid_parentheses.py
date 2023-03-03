#!/usr/bin/env python3

def main():
    print(isValid("()"))


def isValid(self, s: str) -> bool:

    # if the string only contains 1 bracket its false
    if len(s) == 1:
        return False
    
    d = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    stack = []
    
    for chr in s:
        
        if chr in d.keys():
            stack.append(chr)
        elif len(stack) != 0 and chr == d[stack[-1]]:
            stack.pop()
        else:
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False




##############################################################################

if __name__ == "__main__":
    main()
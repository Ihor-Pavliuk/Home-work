#Write a program that reads in a sequence of characters, and determines whether it's parentheses, 
# braces, and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self.__items = []


    def push(self, new_item):
        self.__items.append(new_item)


    def pop(self):
        return self.__items.pop()

    def get(self):
        return self.__items[-1]

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)

def is_balanced(equation):
    stack = Stack()

    for c in equation:
        if c == "[":
            stack.push(c)
        elif c == "]":
            if not stack:
                return False
            stack.pop()
    for d in equation:
        if d == "{":
            stack.push(d)
        elif d == "}":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


x = "[Hello] {Pyphon}"
result  = is_balanced(x)
print("Result", result)

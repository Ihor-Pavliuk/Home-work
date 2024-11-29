#Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

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
        return str(self.__items[::-1])

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)
    
stack = Stack()
stack.push("h")
stack.push("e")
stack.push("l")
stack.push("l")
stack.push("o")
print(stack)
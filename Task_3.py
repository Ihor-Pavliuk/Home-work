# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order. 
# Consider the case in which the element is not found - raise ValueError with proper info Message

# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order. 
# Consider the case in which the element is not found - raise ValueError with proper info Message

class Stack:
    def __init__(self):
        self.__items = []


    def push(self, new_item):
        self.__items.append(new_item)


    def pop(self):
        return self.__items.pop()

    def get(self):
        return self.__items[-1]
    
    def get_from_stack(self, item): 
        temp = []
        found_item = None
        while self.__items:
            last_item = self.__items.pop()
            if last_item == item:
                found_item = last_item
                break
            else:
                temp.append(last_item)
        if found_item is None:
            while temp:
                self.__items.append(temp.pop())
            raise ValueError("Item not found")
        while temp:
            self.__items.append(temp.pop())
        return found_item    

    def __str__(self):
        return str(self.__items[::-1])

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)


class Queue:
    def __init__(self):
        self.__items = []


    def push(self, new_item):
        self.__items.append(new_item)


    def pop(self):
        return self.__items.pop(0)

    def get(self):
        return self.__items[0]
    
    def get_from_stack(self, item):
        temp = []
        found_item = None
        while self.__items:
            first_item = self.__items.pop(0)
            if first_item == item:
                found_item = first_item
                break
            else:
                temp.append(first_item)
        if found_item is None:
            while temp:
                self.__items.append(temp.pop(0))
            raise ValueError("Item not found")
        while temp:
            self.__items.append(temp.pop(0))
        return found_item 

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)
    
stack = Queue()
stack.push("h")
stack.push("e")
stack.push("l")
stack.push("l")
stack.push("o")

print(stack.get_from_stack("o"))
print(stack.get())
print(stack)
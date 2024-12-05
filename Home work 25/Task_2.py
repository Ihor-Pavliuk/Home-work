#Implement a stack using a singly linked list.

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class StackAsSinglLinkendList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def push(self, new_item):
        new_node = Node(new_item) # (1, None); (2, Node(1)); (3, Node(2))
        if not self.root:
            self.root = new_node
        else:
            new_node.next_node = self.root
            self.root = new_node
        self.size += 1

    def pop(self):
        if not self.root:
            raise IndexError("Pop from empty stack")
        value = self.root.data
        self.root = self.root.next_node
        self.size -= 1
        return value
      

    def get(self):
        return self.root.data

    def __str__(self):
        elements = []
        current = self.root
        while current:
            elements.append(current.data)
            current = current.next_node
        return "[" + ", ".join(map(str, elements)) + "]"
    
stack = StackAsSinglLinkendList()
stack.push("h")
stack.push("e")
stack.push("l")
stack.push("l")
stack.push("o")
stack.pop()
print(stack.get())
print(stack)
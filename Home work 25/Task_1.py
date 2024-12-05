# Extend UnsortedList

# Implement append, index, pop, insert methods for UnsortedList. Also implement a slice method, which will take two parameters
# 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def append(self, data):
        new_node = Node(data) # (1, None); (2, Node(1)); (3, Node(2))
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        self.size +=1
        return

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next_node = self.root
            self.root = new_node
            return

        current = self.root
        current_index = 0

        while current and current_index < index - 1:
            current = current.next_node
            current_index += 1

        if not current:
            raise IndexError

        new_node.next_node = current.next_node
        current.next_node = new_node
    def pop(self):
        if not self.root.next_node: 
            value = self.root.data
            self.root = None
            self.size -= 1
            return value
        current = self.root
        while current.next_node and current.next_node.next_node:
            current = current.next_node
        value = current.next_node.data
        current.next_node = None
        self.size -= 1
        return value

    def __str__(self):
        n = self.root
        s = "["
        while n.next_node:
            s += str(n.data) + ", "
            n = n.next_node
        s += str(n.data) + "]"
        return s

    def __len__(self):
        return len(self.root)
    def __getitem__(self, index):
        if isinstance(index, int):  
            if index < 0:
                index += self.size
            if 0 <= index < self.size:
                current = self.root
                for _ in range(index):
                    current = current.next_node
                return current.data
            else:
                raise IndexError("Out of range")
        elif isinstance(index, slice):
            #return self.root[index.start:index.stop] от то вже ці звязні списки))
            result = []
            start = index.start or 0
            stop = index.stop or self.size
            step =  index.step or 1
            current_root = self.root
            current_index = 0
            if start > self.size:
                raise ValueError("Index not found")
            while current_root and current_index < stop:
                if current_index >= start and (current_index - start) % step == 0:
                    result.append(current_root.data)
                current_root = current_root.next_node
                current_index += 1
            return result
        else:
            raise TypeError("Wrong slice")



l = LinkedList()
l.append(1)
l.append(2)
l.append("a")
l.append(3)
l.append(9)
l.append(8)
print(l)
l.pop()
print(l)
print(l[0:6])

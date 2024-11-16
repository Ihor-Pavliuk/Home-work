#Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters: 
# 'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for i in range(start, len(iterable)):
        print(start, iterable[start])
        start += 1

with_index("word", 2)

class With_index:
    def __init__(self, iterable, start = 0):
        self.iterable = list(iterable)
        self.start = start
      
    def __iter__(self):
        return self 

    def __next__(self):
        if self.start >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.start]
        result = (self.start, value) 
        self.start += 1              
        return result
        
a = With_index("word", 2)
for index, value in a:
    print(index, value)
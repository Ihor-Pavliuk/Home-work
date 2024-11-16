# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements
#  using square brackets syntax.
class MyItarableForSquare():
    def __init__(self, *args):
        self.iterable = args
              
    def __iter__(self):
        self.start = 0
        return self 

    def __next__(self):
        if self.start < len(self.iterable):
            value = self.iterable[self.start]
            self.start += 1 
            return value
        else:
            raise StopIteration 
    def __len__(self):
        return len(self.iterable)     
    def __getitem__(self, index):
        if isinstance(index, int):  
            if index < 0:
                index += len(self.iterable)
            if 0 <= index < len(self.iterable):
                return self.iterable[index]
            else:
                raise IndexError("Out of range")
        elif isinstance(index, slice):
            return self.iterable[index.start:index.stop:index.step]
        else:
            raise TypeError("Wrong slice")

       
    
a = MyItarableForSquare(1, 'word', 3, 4, 5, 6, 7, 8, 9)
for value in a:
    print(value)
print(a[-8])
print(a[1])
print(a[0:100:4])
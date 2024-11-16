#Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 'start', 'end',
#  and optional step. Tips: See the documentation for 'range' function
class InRange():
    def __init__(self, start, end, step=1 ):
        self.start = start
        self.stop = end
        self.step = step

    def __iter__(self): # Не впевнений що це вірна умова завдання, тому виконав усі можливі способи на мою думку.
        if self.stop == 0:
            raise StopIteration()
        else:
            current = self.start
            while current < self.stop:
                yield current
                current += self.step
    def in_range(start, end, step=1):
        current = start
        while current < end:
            yield current
            current += step
for i in InRange(1, 10, 2):
    print(i)
def in_range_out_from_class(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step
for i in in_range_out_from_class(1, 10, 2):
    print(i)
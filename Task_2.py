#Implement 2 classes, the first one is the Boss and the second one is the Worker.

#Worker has a property 'boss', and its value must be an instance of Boss.

#You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
#  You should implement a method that allows you to add workers to a Boss. 
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
# use getters and setters instead!

#You can refactor the existing code.

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError()
        if worker not in self.__workers:
            self.__workers.append(worker)

    @property
    def workers(self):
        return self.__workers

    def __repr__(self):
        return f"Boss(id={self.id}, name={self.name}, company={self.company})"

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = None
        self.boss = boss
    

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if not isinstance(boss, Boss):
            raise TypeError("boss must be an instance of Boss.")
        if self.__boss is not None:
            self.__boss.workers.remove(self) 
        self.__boss = boss
        if self not in boss.workers:
            boss.add_worker(self)
    
    def __repr__(self):
        return f"Worker(id={self.id}, name={self.name}, company={self.company}, boss={self.boss.name})"

boss1 = Boss(1, "Mr. Smith", "Tech Corp")
worker1 = Worker(101, "John Doe", "Tech Corp", boss1)
worker2 = Worker(102, "Jane Roe", "Tech Corp", boss1)

print(boss1.workers)
print(worker1.boss)
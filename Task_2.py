import sys

sys.path.append("C:\\Users\\User\\OneDrive\\Робочий стіл\\Python\\Beetroot_128\\Home_work_9\\sys.py")
for i in sys.path:
    del sys.path[0]
    del sys.path[0]
    del sys.path[0]
print (sys.path)
# Я можу видалити всі шляхи до sys, окрім пари, з дерикторії в якій я запускаю модулі
# на функціонал це ніяк не вплинуло

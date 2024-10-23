from mymod import test, test_2

test("data.txt")
test_2("data.txt")

#Does your PYTHONPATH need to include the directory where you created mymod.py?
#Так, потрібен, оскільки я працюю в каталозі BEETROOT_128, а файл mymod міститься в підкаталозі Home_work_9, і його не знаходить. Рішення є два, або прописувати шлях до файлу, або скопіювати до каталогу з якого я працюю. я не став заморачуватися з import os і скопіював файл.

#Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice; if you’re feeling ambitious, you may be able to improve this by passing an open file object into the two count functions (hint: file.seek(0) is a file rewind).
# для цього доведеться 2 функції об'єднати в одну, і використати file.seek(0) для повернення на нульовий індекс 
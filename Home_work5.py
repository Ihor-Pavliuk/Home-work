import random # як же мене бісить перетворення input в цифри

#Task1
a = random.randint(1,10) 
print("Зіграємо в гру")
while True:
    b = input("Вгадай число від 1 до 10!")
    if b.isdigit():
        b = int(b)
        if 1 <= b <= 10:
            if b == a:
                print("Вітаю! Ти вгадав!")
                break 
            else:
                print("Не вгадав, спробуй ще раз.")
        else:
            print("Будь ласка, введи число від 1 до 10")
    else:
        print("Будь ласка, введи число від 1 до 10")

#Task 2
name = input("Вкажіть Вашe ім'я ")
age = input("Вкажіть Ваш вік")
age = int(age)
print(f"Вітаю {name}! В наступний Ваш день народження Вам буде {age + 1} років")

#Task 3 # перетворення в зі списку в рядок, також бісячка))
word = input("Напиши слово і отримає 5 варіантів тарабарщини з букв твого слова")
count = 0
word2 = list(word)
while count < 5:
    random.shuffle(word2)
    print(''.join(word2))
    count += 1
    continue
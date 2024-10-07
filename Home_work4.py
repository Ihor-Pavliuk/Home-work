# Task 1
sample_string1 = "helloworld"
sample_string2 = "my"
sample_string3 = "x"
if len(sample_string1) >=2:   
    print (sample_string1[0: 2] + sample_string1[-2:])
else:
    print (" ")
if len(sample_string2) >=2:   
    print (sample_string2[0: 2] + sample_string2[-2:])
else:
    print (" ")
if len(sample_string3) >=2:   
    print (sample_string3[0: 2] + sample_string3[-2:])
else:
    print (" ")

#Task 2
phone_numder = 1234567890 # тут є проблема, якщо ввести букви, видає помилку....
if phone_numder is int(phone_numder):
    if len(str(phone_numder)) == 10:
        print("Дякуємо за довіру")
    else: 
        print ("Будь-ласка, введіть коректні данні")

#Task 3
answer = input("Скільки буде 2+2= ?") #якже я замахався забувши що input це завжди рядки!
while int(answer) != 4:
    print(answer + " не вірно, спробуй ще раз")
    answer = input("Скільки буде 2+2= ?")
if int(answer) == 4:
        print("Вітаю, це вірна відповідь")

#Task 4
name = "ігор"
user_name =input('Стій хто йде?').lower()
print (name == user_name)



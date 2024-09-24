# Task1
import datetime # дякую GPT
days_ua = {
    'Monday': 'понеділок',
    'Tuesday': 'вівторок',
    'Wednesday': 'середа',
    'Thursday': 'четвер',
    'Friday': 'пʼятниця',
    'Saturday': 'субота',
    'Sunday': 'неділя'
} # знову дякую GPT
today = datetime.datetime.today().strftime('%A')
name = 'Ігор'
text_1 = 'Привіт'
text_2 = 'Вже'
text_3 = 'досить задротити в ігри, задроть в Python!' 
print (text_1 + ' ' + name + '. ' + text_2 + ' ' + days_ua[today] + ' ' + text_3, '\n')
# це не по шаблону задання, але так цікавіше
# Task2
first_name = 'ігор'
last_name = 'павлюк'
hello = 'привіт'
print (hello.title(),first_name.title(),last_name.title(), sep=' ', end='!\n')
# Task3
a = 3
b = 2
print ('2 + 3 = ' + str(a + b)) #Addition
print ('2 - 3 = ' + str(a - b)) #Subtraction
print ('3 / 2 = ' + str(a / b)) #Division
print ('2 * 3 = ' + str(a * b)) #Multiplication
print ('3 ** 2 = ' + str(a ** b)) #Exponent
print ('3 % 2 = ' + str(a % b)) #Modulus
print ('3 // 2 = ' + str(a // b)) #Floor division
#або так
print (f'{a} + {b} = {a + b}')
print (f'{a} - {b} = {a - b}')
print (f'{a} / {b} = {a / b}')
print (f'{a} * {b} = {a * b}')
print (f'{a} ** {b} = {a ** b}')
print (f'{a} % {b} = {a % b}')
print (f'{a} // {b} = {a // b}')


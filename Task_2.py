def your_math():
    try:
        a = int(input("To see squared a divided by b. Please write a = "))
        b = int(input("Please write b = "))  
        result = (a ** 2) / b
        print(f"Your result = {result}")
    except ValueError:
        print("Please write only numbers")
    except ZeroDivisionError:
        print("b cannot = 0")
your_math()
# я тут відкрив для себе багато цікавого) наприклад result, не винесеш в return, та й взагалі return тут зайвий
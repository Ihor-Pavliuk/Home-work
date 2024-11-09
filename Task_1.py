def count_variables():
    a = 10
    b = 20
    c = a + b
    d = "Hello, Teacher!"
    
    # Підраховуємо кількість локальних змінних на цей момент
    return len(locals())

print(count_variables())
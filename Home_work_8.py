# Task 1

def movie (my_favorite_film):
    return f"My favorite movie is named {my_favorite_film}"
print(movie('The Shawshank Redemption'))

# Task 2

def make_country(name, capital):
    name = name.title()
    make_country= {}
    make_country[name] = capital.title()
    return print(make_country[name])
make_country("ukraine", "kyiv")

# Task 3

def make_operation(x, *agrs):
    if x == '+':
        return_value =0
        for num in agrs:
            return_value += num
        return return_value
    if x == '-':
        return_value = agrs[0]
        for num in agrs[1:]:
            return_value -= num
        return return_value
    if x == '*':
        return_value = 1 
        for num in agrs:
            return_value *= num
        return return_value
    else: 
        return print("Wrong argments")
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
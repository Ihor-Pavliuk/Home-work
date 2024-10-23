# я зробив так тому що так простіше, низче зроблю так як вимагає умова задачі, без with as
def count_lines(name) : 
    with open(name, "r") as file_open:
        lines = file_open.readlines()
    return print (f'lines =  {len(lines)}')
def count_chars(name) :
    with open(name, "r") as file_open:
        chars = file_open.read()
        numbers_of_characters = 0
        for i in chars:
            numbers_of_characters += 1
    return print(f'numbers of characters = {numbers_of_characters}')

def test(name) :
    count_lines(name)
    count_chars(name)
    return
# без with as
def count_lines_2(name) :
    file_open = open(name, "r")
    lines = file_open.readlines()
    file_open.close()
    return print(f'lines =  {len(lines)}')
def count_chars_2(name) :
    file_open = open(name, "r")
    chars = file_open.read()
    numbers_of_characters = 0
    for i in chars:
        numbers_of_characters += 1
    file_open.close()
    return print(f'numbers of characters = {numbers_of_characters}')
def test_2(name) :
    count_lines_2(name)
    count_chars_2(name)
    return

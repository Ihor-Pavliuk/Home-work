# Task 1

some_text = "Make a program that has some sentence some"
some_text_split_and_lower= some_text.lower().split()
dict_with_word_and_number_of_repeat = {}
for i in some_text_split_and_lower:
    if i in dict_with_word_and_number_of_repeat:
        dict_with_word_and_number_of_repeat[i] += 1
    else:
        dict_with_word_and_number_of_repeat[i] = 1
print (dict_with_word_and_number_of_repeat)

# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_prise = {}
for key, value in stock.items():
    total_prise[key] = value * prices[key]
print(total_prise)

# Task 3

new_list = []
for i in range(1, 11):
    j = i ** 2
    new_list.append([i, j])
print (new_list)

# Task 4

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_days = {}
revers_dict_days = {}
numders = 1
print()
for i in days:
        dict_days[numders] = i
        numders += 1
print(dict_days)
for k, v in dict_days.items():
        revers_dict_days[v] = k
print(revers_dict_days)

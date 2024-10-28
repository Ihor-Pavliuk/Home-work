import json
phonebook = {}
def add(phonebook_name, first_name, last_name, number, city_or_country): 
    with open('my_phonebook.json', 'r') as file:
        phonebook = json.load(file)
        if phonebook_name in phonebook: # не працює так як повинно
            print("Alredy exist")
        else:
            phonebook[phonebook_name] = {"First_name": first_name, "Last_name": last_name, "Full_name": first_name + " " + last_name, "number":number, "city_or_country":city_or_country}
            with open('my_phonebook.json', 'w') as file:
                json.dump(phonebook, file, indent=4)
add(11, "a", "b", 4, 5)
add(25, "a", "b", 4, 6)

#add(6, "c", "b", 7, 8)
#add(9, "g", "w", 11, 12)

def search_by_first_name(first_name):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("First_name") == first_name:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
#search_by_first_name("f")
def search_by_first_name(first_name):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("First_name") == first_name:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
def search_by_last_name(last_name):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("Last_name") == last_name:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
def search_by_full_name(full_name):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("Full_name") == full_name:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
def search_by_city_or_country(city_or_country):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("city_or_country") == city_or_country:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
def search_by_number(number):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        already_in = False
        for k, v in data.items():
            if v.get("number") == number:
                print (f'Found phonedook {k} and data {v}') 
                already_in = True
        if not already_in :
            print("Not found")
def delete_phone_book_for_number(telehone_number):
    with open('my_phonebook.json', 'r') as file:
        data = json.load(file)
        to_del = []
        for k, v in data.items():
            if v.get("number") == telehone_number:
                to_del.append(k) 
    for k in to_del:
        del data [k]
    with open('my_phonebook.json', 'w') as file:
        json.dump(data, file, indent=4)
    
#delete_phone_book_for_number(7)
def update_record_for_given_telephone_number(phonebook_name, first_name, last_name, number, city_or_country):
    with open('my_phonebook.json', 'r') as file:
        new_data = {}
        data = json.load(file)
        for k, v in data.items():
            if v.get("number") == number:
                new_data[k] = {"First_name": first_name, "Last_name": last_name, "Full_name": first_name + " " + last_name, "number":number, "city_or_country":city_or_country} 
    data.update(new_data)
    data[phonebook_name] = data.pop(k)
    with open('my_phonebook.json', 'w') as file:
        json.dump(data, file, indent=4)

def close():
    exit()
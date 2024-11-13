import json 
from pprint import pprint
phonebook_filename = 'my_phonebook.json'
try:
    with open(phonebook_filename, 'r') as file:
        phonebook = json.load(file)
except FileNotFoundError:
    print(f"Error:'{phonebook_filename}' does not exist.")
    phonebook = {}
except json.JSONDecodeError:
    print(f"Error:'{phonebook_filename}' is not JSON.")
    phonebook = {}
def add(phonebook_name, first_name, last_name, number, city_or_country): 
    for k, v in phonebook.items():
        if v.get("number") == number:
            print("Alredy exist")
            return
    phonebook[phonebook_name] = {
        "First_name": first_name, 
        "Last_name": last_name, 
        "Full_name": f"{first_name} {last_name}", 
        "number":number, 
        "city_or_country":city_or_country
        }
    print(f'New contact added')
add("new_contact", "John", "Doe", 123456789, "New York")

def search_by_first_name(first_name):
    already_in = False
    for k, v in phonebook.items():
        if v.get("First_name") == first_name:
            print (f'Found phonedook {k} and data {v}') 
            already_in = True
    if not already_in :
        print("Not found")

def search_by_last_name(last_name):
    already_in = False
    for k, v in phonebook.items():
        if v.get("Last_name") == last_name:
            print (f'Found phonedook {k} and data {v}') 
            already_in = True
    if not already_in :
        print("Not found")
def search_by_full_name(full_name):
    already_in = False
    for k, v in phonebook.items():
        if v.get("Full_name") == full_name:
            print (f'Found phonedook {k} and data {v}') 
            already_in = True
    if not already_in :
        print("Not found")
def search_by_city_or_country(city_or_country):
    already_in = False
    for k, v in phonebook.items():
        if v.get("city_or_country") == city_or_country:
            print (f'Found phonedook {k} and data {v}') 
            already_in = True
    if not already_in :
        print("Not found")
def search_by_number(number):
    already_in = False
    for k, v in phonebook.items():
        if v.get("number") == number:
            print (f'Found phonedook {k} and data {v}') 
            already_in = True
    if not already_in :
        print("Not found")
def delete_phone_book_for_number(telehone_number):
    to_del = []
    for k, v in phonebook.items():
        if v.get("number") == telehone_number:
            to_del.append(k) 
    for k in to_del:
        del phonebook[k]

def update_record_for_given_telephone_number(phonebook_name, first_name, last_name, number, city_or_country):
    for k, v in phonebook.items():
        if v.get("number") == number:
            if phonebook_name != k:
                phonebook[phonebook_name] = phonebook.pop(k)
            phonebook[phonebook_name] = {
                "First_name": first_name, 
                "Last_name": last_name, 
                "Full_name": f"{first_name} {last_name}", 
                "number":   number, 
                "city_or_country":  city_or_country
            } 
            print("Contact update")
            return  

def close():
    with open('my_phonebook.json', 'w') as file:
        json.dump(phonebook, file, indent=4)
        print("Phonebook saved")
    exit()

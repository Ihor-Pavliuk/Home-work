#Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write
#  tests using unittest library
import unittest
from unittest.mock import patch, mock_open
import Phonebook


class MyPhoneBookTest(unittest.TestCase):
    
    def setUp(self):
        
        Phonebook.phonebook = {
        "existing_contact": {
            "First_name": "John", 
            "Last_name": "Doe", 
            "Full_name": "John Doe", 
            "number": 123456789, 
            "city_or_country": "New York"
        }
    }

       

    def test_add(self): #Тест працює, але прінтує "Alredy exist" перед перевіркою ніби контакт вже існує
        with patch("builtins.print") as mocked_print:
            Phonebook.add("new_contact", "Jane", "Smith", 987698750, "London")
            self.assertIn("new_contact", Phonebook.phonebook)
            self.assertEqual(Phonebook.phonebook["new_contact"]["First_name"], "Jane")
            mocked_print.assert_any_call("New contact added")
    
    
    def test_search_by_first_name(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.search_by_first_name("John")
            mocked_print.assert_any_call("Found phonedook existing_contact and data {'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'number': 123456789, 'city_or_country': 'New York'}")
            Phonebook.search_by_first_name("Jane")
            mocked_print.assert_any_call("Not found")

    def test_search_by_last_name(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.search_by_last_name("Doe")
            mocked_print.assert_any_call("Found phonedook existing_contact and data {'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'number': 123456789, 'city_or_country': 'New York'}")
            Phonebook.search_by_last_name("Smith")
            mocked_print.assert_any_call("Not found")

    def test_search_by_full_name(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.search_by_full_name("John Doe")
            mocked_print.assert_any_call("Found phonedook existing_contact and data {'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'number': 123456789, 'city_or_country': 'New York'}")
            Phonebook.search_by_last_name("Jane Smith")
            mocked_print.assert_any_call("Not found")

    def test_search_by_city_or_country(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.search_by_city_or_country("New York")
            mocked_print.assert_any_call("Found phonedook existing_contact and data {'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'number': 123456789, 'city_or_country': 'New York'}")
            Phonebook.search_by_city_or_country("London")
            mocked_print.assert_any_call("Not found")


    def test_search_by_number(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.search_by_number(123456789)
            mocked_print.assert_any_call("Found phonedook existing_contact and data {'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'number': 123456789, 'city_or_country': 'New York'}")
            Phonebook.search_by_number(987698750)
            mocked_print.assert_any_call("Not found")

    def test_delete_phone_book_for_number(self):
        Phonebook.delete_phone_book_for_number(123456789)
        self.assertNotIn("existing_contact", Phonebook.phonebook)

    def self_update_record_for_given_telephone_number(self):
        with patch("builtins.print") as mocked_print:
            Phonebook.update_record_for_given_telephone_number("new_contact", "Jane", "Smith", 123456789, "London")
            self.assertEqual(Phonebook.phonebook["new_contact"]["First_name"], "Jane")
            mocked_print.assert_any_call("Contact update")

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    @patch("builtins.exit")  # Я два дні не міг зрозуміти чому в мене помилка яка ругається на exit() 
    def test_close(self, mock_exit, mock_json_dump, mock_open_file):
        test_phonebook = {
            "Alice": {
                "First_name": "Alice",
                "Last_name": "Smith",
                "Full_name": "Alice Smith",
                "number": "12345",
                "city_or_country": "Wonderland"
            }
        }

        with patch("Phonebook.phonebook", test_phonebook):
            Phonebook.close()
            mock_open_file.assert_called_once_with('my_phonebook.json', 'w')
            mock_json_dump.assert_called_once_with(test_phonebook, mock_open_file(), indent=4)
            mock_exit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
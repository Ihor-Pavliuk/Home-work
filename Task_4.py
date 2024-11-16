#Custom exception

#Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its functionality 
# to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages 
# to file

import datetime

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"[{timestamp}]: {msg}\n")
try:
    raise CustomException("Magic")
except CustomException as info:
    print (f'Error {info}')
CustomException("magic")

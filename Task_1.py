# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed 
# to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email 
# string.

#Email validations:

#Valid email address format 

#Email address 
import re 
class Validate:
    def __init__(self, email):
        self.__email = self.__validate(email)
        
    @staticmethod    
    def __validate(email):
        #contains_to_prefix =  ['"', "$", "%", "&", "'", "*", "+", "/", "=", "?", "^",
                              #  "`", "{", "|", "}", "~", "[", "]", "(", ")", "#", ";", ":",] # "\" can write in code for validate
        double_pattern_for_email_prefix = r'[-_.]{2,}'
        forbitten_pattern_for_email_prefix = r'[\"$%&\'*+/=?^`{|}~\[\]()#;:\\]'
        forbitten_pattern_for_email_domain = r'[\"$%&\'*+/=?^`{|}~\[\]()#;:\\_\.]'
        prefix = None
        domain = None
        domain_before_dot = None 
        domain_after_dot = None
        allowed_domains = {"com", "org", "net", "ua"}
        if not isinstance(email, str):
            raise TypeError("Email is not str.")
        if "@" not in email:
            raise ValueError("Wrong email adress, adress must have '@'.")
        elif isinstance(email, str):
            prefix, domain = email.split('@')
            #for i in prefix:
                #if i in contains_to_prefix:
                    #raise ValueError("forbidden sign")
            if re.search(double_pattern_for_email_prefix, prefix):
                raise ValueError("Double either -, or _, or . !!!")
            if re.search(forbitten_pattern_for_email_prefix, prefix):
                raise ValueError("Forbitten symbols")
            if "." not in domain:
                raise ValueError("Invalid email domain: missing '.'.") 
            domain_before_dot, domain_after_dot = domain.split(".", 1)
            if re.search(forbitten_pattern_for_email_domain, domain_before_dot):
                raise ValueError("Wrong email") 
            if domain_after_dot == "ru":
                raise ConnectionResetError("Please stay in place, in few minuts, some interesting people wanna speek with you!")
            if domain_after_dot not in allowed_domains:
                raise ValueError("Wrong email")    
        if prefix == "":
            raise ValueError("Wrong email")
        if prefix[0] == '_' or prefix[0] == "." or prefix[0] == "-":
                raise ValueError("First symbon mast be letters or numbers")
        if prefix[-1] == '_' or prefix[-1] == "." or prefix[-1] == "-":
                raise ValueError("Last symbon mast be letters or numbers")
        return email

    @property
    def email(self):
        return self.__email
email = Validate("abs@example.com")
#wrong_email = Validate("testexample.com")
email = Validate("123abc@example.com")
print(email.email)
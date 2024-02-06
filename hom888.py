import re

def validate_home_phone(phone_number):

    return re.match(r'^\d{7,10}$', phone_number) is not None

def validate_mobile_phone(phone_number):

    return re.match(r'^\+?\d{10,12}$', phone_number) is not None

def validate_email(email):

    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validate_full_name(full_name):

    return re.match(r'^[a-zA-Zа-яА-ЯёЁ]{2,20}( [a-zA-Zа-яА-ЯёЁ]{2,20}){2}$', full_name) is not None


home_phone = input("Enter home phone number: ")
mobile_phone = input("Enter mobile phone number: ")
email = input("Enter email: ")
full_name = input("Enter full name: ")

print("Home phone number:", validate_home_phone(home_phone))
print("Mobile phone number:", validate_mobile_phone(mobile_phone))
print("Email:", validate_email(email))
print("Full name:", validate_full_name(full_name))
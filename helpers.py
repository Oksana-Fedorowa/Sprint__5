import random
import string

def create_random_email():
    email_base = "oksana_fedorowa_11_"
    random_digits = ''.join(random.choices(string.digits, k=3))
    domain = "@ya.ru"
    return email_base + random_digits + domain

def create_random_password(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))
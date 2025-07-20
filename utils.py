import string
import random


def generate_password(obj):
    symbols = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.sample(symbols, 16))
    obj.setText(generated_password)

import random
from datetime import timedelta, date

def random_phone():
    return f"+79{random.randint(10000000, 99999999)}"

def random_date_for_delivery():
    today = date.today()
    offset = random.randint(1, 14)
    return (today + timedelta(days=offset)).strftime("%d.%m.%Y")

def random_in_list(list):
    return random.choice(list)

def random_boolian():
    return random.choice([True, False])
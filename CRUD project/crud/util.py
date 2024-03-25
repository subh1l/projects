import random
import string

def random_string(length):
    result = "".join(random.choice(string.ascii_letters) for i in range(length))
    return result
from random import choice
from string import digits, ascii_uppercase, ascii_lowercase

COLLECTIONS = str(digits + ascii_uppercase + ascii_lowercase)
def generated_code():
    code = ''
    for i in range(6):
        code += choice(COLLECTIONS)
    return code


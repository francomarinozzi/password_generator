import random
import string 


def create_psw(psw_len):
    password = ""
    if psw_len == 1:
        password += str(random.randint(0,9))
    elif psw_len %2 == 0:
        password += create_psw(psw_len -1) + random.choice(string.ascii_letters)
    else:
        password += create_psw(psw_len -1) + str(random.randint(0,9))
    return password


def create_psw_txt():
    doc = open("password.txt", "w")
    doc.write(create_psw(10))
    doc.close()

create_psw_txt()
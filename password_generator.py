import random

def password_generator():
    uppers = [chr(random.randint(65, 90)) for i in range(3)]
    lowers = [chr(random.randint(97, 122)) for i in range(3)]
    numbers = [chr(random.randint(48, 57)) for i in range(3)]
    chars = chr(random.randint(33, 47)) + chr(random.randint(58, 64))
    password = "".join(uppers) + "".join(numbers) + "".join(lowers) + chars
    passw_list = list(password)
    random.shuffle(passw_list)
    return "".join(passw_list)

#generate a password simply by calling the function password_generator()
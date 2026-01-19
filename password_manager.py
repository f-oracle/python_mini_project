from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = raw_input('what is the master password? ')  # type: ignore
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt',  'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = raw_input('Account Name: ')  # type: ignore
    pwd = raw_input('Password: ')  # pyright: ignore[reportUndefinedVariable]

    with open('password.txt',  'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")


while True:
    mode = raw_input(
        'Would you like to add a new password or view existing ones (view, add)?, press q to quit? ').lower()  # type: ignore
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode.')
        continue

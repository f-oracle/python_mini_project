pwd = raw_input('what is the master password? ') # type: ignore

def view():
    pass

def add():
    name = raw_input('Account Name: ') # type: ignore
    pwd =  raw_input('Password: ') # pyright: ignore[reportUndefinedVariable]

    with open('password.txt',  'a') as f:
        f.write(name + " " + pwd)

while True:
    mode = raw_input('Would you like to add a new password or view existing ones (view, add)?, press q to quit? ').lower() # type: ignore
    if mode == 'q':
        break
    if mode == "view":
       view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode.')
        continue
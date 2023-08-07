def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception("The password must be at least 8 characters long.")
    elif not re.search("[a-z]",psw):
        raise Exception("The password must contain lowercase letters.")
    elif not re.search("[A-Z]",psw):
        raise Exception("The password must contain uppercase letters.")
    elif not re.search("[0-9]",psw):
        raise Exception("The password must contain digit.")
    elif not re.search("[/s]",psw):
        raise Exception("The password must not contain spaces.")

password=input('your password: ')

try:
    check_password(password)
except Exception as ex:
    print(ex)
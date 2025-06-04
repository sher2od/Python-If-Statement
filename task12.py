from getpass import getpass

currect_password = "1234"

current_password = getpass()

if currect_password == current_password:
    print("sayitga kirdi")


else:
    print("password xato")



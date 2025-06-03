email = input("Email >> ")

if (
    "@" in email and
    "." in email and
    " " not in email 
):
    print("To'g'ri email")
else:
    print("Email xato!")

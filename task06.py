phone_number = input("Telefon kodini kiriting ")

if len(phone_number) == 2 and phone_number.isdigit():
    kod = int(phone_number)

    if kod in [90, 91]:
        print("usell")
    elif kod in [93, 94]:
        print("beeline")
    elif kod in [88, 99]:
        print("mobiuz")
    else:
        print("Operator topilmadi")
else:
    print("Notogri kod kiritildi")

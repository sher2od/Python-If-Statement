harf = input("Biror harf kiriting: ")

if len(harf) == 1:
    kod = ord(harf)
    
    if 65 <= kod <= 90:
        print(harf, "— bu katta harf")

    elif 97 <= kod <= 122:
        print(harf, "— bu kichik harf")

    else:
        print(harf, "— bu harf emas")

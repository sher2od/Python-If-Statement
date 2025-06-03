# Foydalanuvchidan omonat summasini olish
summasi = float(input("Omonat summasini kiriting (so'mda): "))

# Foiz stavkasini aniqlash
if summasi < 100000:
    foiz = 5
elif 100000 <= summasi <= 500000:
    foiz = 7
else:
    foiz = 10

# Natijani chiqarish
print(f"Omonat summasiga {foiz}% foiz qollaniladi.")

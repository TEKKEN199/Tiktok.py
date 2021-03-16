import sys
import time

# ================================================
name = input("name File:")
uesr = ''  # اليوزر المراد التخمين عليه بين النقطتين اكتبه
chars2 = 'qazwsxedccrfvtgbyhnujmikolp1234567890'  # ارقام واحرف لو ترغب
amount = input('كم عدد كلمات المرور؟')
amount = int(amount)

length2 =input('ما طول كلمة المرور التي تريدها؟')
length2 = int(length2)

for password in range(amount):
    password = ''

    for item in range(length2):
        password = ''
    for item in range(length2):
        password += random.choice(chars2)

        X = str(uesr + password)
    print(X)
    with open(name, 'a') as x:
        x.write(X + '\n')

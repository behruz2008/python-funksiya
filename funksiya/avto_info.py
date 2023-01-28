# def - bu funksiyaning kalit so'zi
# avto_info - funksiyaning o'zgaruvchisi
# qavs ichidagi qiymatlar - avto_info funksiyasining argument qiymatlari

def avto_info(kompaniya, model, rangi, yili, narxi):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'yili':yili,
            'narxi':narxi
            }
    # return avto degan o'zgaruvchini obyektlarini yig'ib o'ziga qaytaryabdi
    return avto
# console - print ya'ni chop qilish berilganda, obyektni korsatuvchi oyna

print("Avtomobillar ro'yxatini shakillantirish :")
# avtolar = [] - bo'sh massiv, maqsadi - bo'sh holatida, ichiga berilgan qiymatlarni o'ziga qabul qilib oladi
avtolar = []
# while True - doimiy takrorlanib boradigan abadiy takrorlanish sikli
while True:
    
    print("Avtomobil ma'lumotlarini kiriting : ",
    end='')
    # end - o'zidan keyin bitta qator tashlab beradi
    kompaniya = input("Ishlab chiqarilgan kompaniya nomi = ")
    model = input("Avtomobil modeli = ")
    rangi = input("Avtomobil rangi = ")
    yili= input("Avtomobil yili = ")
    narxi = input("Avtomobil narxi = ")
    # avtolar - bo'sh ro'yxatga terish
    # append - funksiya metodi bo'lib, olgan qiymatni keyingisiga qo'shib beradi
    # (avto_info - asosiy bazadagi kompaniya, model, rang, yil va narxni olib avtolar ga qo'shish degani)
    avtolar.append(avto_info(kompaniya, model, rangi, yili, narxi))
    
        
    javob = input("Yana avtomobil qo'shasizmi Y/N = ")
    # if - shart operatori bo'lib, javob = N ga teng bo'lsa break - dastur to'liq to'xtaydi
    if javob == "N":
        break
    
    print("Barcha avtomobillar ro'yxati : \n __________________________________________________")
#  kompaniya nomi kiritiladi 
# f string = f"{}"" maqsadi, obyektlarni alohida qo'shtirnoq, vergullarsiz bitta qo'shtirnoq orqali ham chaqirib ham izoh berish mumkin
print(f"Avtomobil kompaniyasi :   {kompaniya} \n"
      f"Avtomobil modeli : {model} \n"
      f"Avtomobil rangi : {rangi} \n"
      f"Avtomobil chiqarilgan til:  {yili}  - yil \n"
      f"Avtomobil narxi:    {narxi} \n"
      )
   



# Vazifa talabalar jurnali funksiyasi



# ism
# familiya
# yoshi
# nechanchi kurs
# institut
# turar joy

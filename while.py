

# Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir ro'yxatni olib, ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni takrorlar edi. while ham takrorlash operatori bo'lib, for dan farqli ravishda, toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi.  
# while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.


# while yordamida 5 gacha sanash algoritmi

son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end=' ') # son ni konsolga chiqaramiz,
    son = son+1 # songa 1 qo'shamiz.
    

###############################################################################


# while va input()



# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")



# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)


###############################################################################



# Ishora (flag)


# Yuqoridagi dasturda dasturni to'xtatish uchun yagona shartni tekshirdik (qiymat!='exit'), katta dasturlarda bir emas bir nechta shartlarni tekshirish, va ulardan biri bajarilgan taqdirda dasturni to'xtatish talab qilinishi mumkin. 
# Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin. Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri bajarilganda ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi. 


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


###############################################################################


# BREAK OPERATORI

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)





###############################################################################


# Misol uchun:

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


# CONTINUE OPERATORI



# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")



###############################################################################



# Misol uchun:

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)



# Respect
# Tsikllar bilan ishlashda abadiy tsikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak. Abadiy tsiklga turli mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri shart, o'zgarmas qiymat, kodlar ketma-ketligida xatolik va hokazo. 
# Kelin ba'zi misollarni ko'ramiz:



# infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)


###############################################################################




# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        
        
        
        
        
        

# password = ''

# while True:
#     password = input('Parolinggizni kiriting : ')

#     if len(password) < 4:
#         print('Parolinggiz kam')
#         continue
#     else:
#         print(f'Siz kiritgan parol: {password}')
#         break

# print(password)

# num = 0
# while True:
#     try:
#         num = int(input("1-4 oralig'idagi parol : "))
#     except ValueError:
#         print("1-4 orasidagi parol kiriting : ")
#         continue
#     if num >= 1 and num <= 5:
#         print(f'Siz kiritigan parol: {num}')
#         break
#     else:
#         print(" Faqat 1-4 oralig'idagi parol kiritishinggiz kerak")

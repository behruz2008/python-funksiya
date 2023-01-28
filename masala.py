


# sonlarga oid masalalar:


###########################################################################################


# 1) Sm qiymat kiriting degan so'rov kelganda, uni dm va metrda ifodalovchi algoritm tuzilsin

# Masalan : sm kiriting = 100
# Javob : 100sm == 10dm, 100sm == 1m

# sm = input("Sm qiymatni kiriting = ")
# dm = sm/10
# metr = sm/100
# print(dm,sm)

###########################################################################################

# 3 xonali Son kiritish so'ralganida, uni kiritgach, yuzlar, o'nlar va birlar xonasiga yaxlitlab yig'indi ko'rinishda qaytarsin
# Masalan - SOn kiriting = 239
# Javob - 200 + 30 + 9

# son = (input("Son kiriting == "))
# s = son[0] + "00 + " + son[1] + '0 + ' + son[2]
# print(s)

###########################################################################################

# Shart operatoriga oid masalalar:

# 1) Butun son kiritish so'ralsin, agar qiymat musbat bo'lsa, 1ga oshirsin, manfiy va 0 bo'lsa o'z holida qolsin,
# Masalan: son = 12 
# Javob = 13

# son = int(input("Son kiriting = "))
# if son > 0:
#     print(son+1)
# else:
#     print(son)

###########################################################################################


# 2) 3ta son kiritish so'ralsin, ular ichidagi musbat va manfiylar, eng katta va kichiklarni aniqlansin

# Masalan birinchi = 25
# ikkinchi = -30
# uchinchi = 40
# Javob = Musbat - 40, 25
# Manfiy = -30


# son1 = int(input("Birinchi = "))
# son2 = int(input("Ikkinhi = "))
# son3 = int(input("Uchinchi = "))
# if son1>0:
#     print("Musbat = ",son1)
    
# if son2>0:
#     print("Musbat = ",son2)
    
# if son3>0:
#     print("Musbat = ",son3)

# if son1<0:
#     print("Manfiy = ",son1)
    
# if son2<0:
#     print("Manfiy = ",son2)
    
# if son3<0:
#     print("Manfiy = ",son3)

# else:
#     print("Xatolik")


###########################################################################################


# Uchta son kiritish so'ralsin, ulardan 2tasini eng katta yig'indisini qaytarsin

# Masalan : son1 = 100, son2 = 200, son3 = 300 , eng katta yig'indi = 500

# son1 = int(input("Birinchi = "))
# son2 = int(input("Ikkinchi = "))
# son3 = int(input("Uchinchi = "))
# print("Bu qiymatlardagi eng katta yig'indi = ",son1+son2+son3-min(son1,son2,son3))
# print("Eng kichik yig'indi", son1+son2,son3 - max(son1,son2,son3))



###########################################################################################


# Faqat 3 xonali sonlarni qabul qiladigan shart algoritmi tuzilsin

# a=input("Faqat 4 xonali son kiriting = ")
# if len(a)==4:
#     print("True")
# else:
#     print("False")


###########################################################################################


#  Bankdan qarz olish summasi kiritish soralsin, va foiz stavkasi ham soralsin. yil davomida bir xil 12ga taqsimlangan foiz summasining qiymatini qaytaradigan algoritm tuzilsin

# Masalan:

# summa = 100 000 000 
# foiz : 12
# Natija: 
# 1-oy = 812 000 
# 2 - oy = 812 000 .............


# summa = float(input("Summani kiriting = "))
# foiz = float(input("Foizni kriiting = "))
# jadval = (summa + (summa*foiz)/100)/12
# for i in range(12):
#     print("{0} - oy = {1}".format(i+1, jadval))


###########################################################################################



# Moslashuvchan funskiyalar - funksiyaning argumentlariga islatgan qiymat berish va ularni obyektlarga yo'naltirish vazifasini bajarib beradi



# Moslashuvchan funksiyalarning 2 xil metodi bor :

# 1) *args - arguments
# 2) **kwargs - keyword arguments


# def main(son1,son2, *args):
#    return son1, son2, args
# a = main(1,2,3)
# print(a)

# def qoshish(*args):
#     print(args, type(args))

# qoshish(2+3)



def main(son1,son2, *args):
    return son1, son2, *args
a= int(1+ 2+ 3)
print(a)
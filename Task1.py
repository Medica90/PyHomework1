#Найдите сумму цифр трехзначного числа.

a = int(input('Введите трехзначное число: '))
summa = 0
while a>0:
    c = a%10
    summa = summa+c
    a = a//10
print(summa)
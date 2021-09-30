# 2.2
list1 = input("Введите элемент списка >>>").split()

for i in range(0, len(list1), 2):
    k = num1 = list1[i]

    if i + 1 < len(list1):
        num2 = list1[i + 1]
        num1 = num2
        num2 = k
        print(num1, num2, end=' ')
    else:
        print(num1)
# 2.6

products = []
name_1 = []
price_1 = []
quantity_1 = []
ed_1 = []

print("How many items do you want to deposit? >>> ")
n = int(input())

if n <= 0:
    for i in range(0, n):
        name = input("Введите название товара >>> ")
        price = input("Введите цену товара >>> ")
        quantity = input("Введите количество товара >>> ")
        ed = input("В чем измеряется количестов (шт., единиц и т.п) >>> ")
        k = (i, {"название": name, "цена": price, "количество": quantity, "ед.": ed})

    products.append(k)
    name_1.append(name)
    price_1.append(price)
    quantity_1.append(quantity)
    ed_1.append(ed)

    print("Аналитика", end='\n')
    analysis = [{"название": name_1,
                 "цена": price_1,
                 "количество": quantity_1,
                 "ед.": ed_1}]
    print(analysis)

else:
    print("Try to enter another number of items")
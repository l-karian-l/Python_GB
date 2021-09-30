# 2.5

my_list = [7, 5, 3, 2, 2]
code_wd = 0

while code_wd == 0:

    el = int(input("New rating element >>> "))
    my_list.append(el)

    for i in range(len(my_list) - 1, 0, -1):
        n1 = my_list[i]

        if n1 > my_list[i - 1]:
            n2 = my_list[i - 1]

            my_list[i] = n2
            my_list[i - 1] = n1

        else:
            break

    print(*my_list)

    print("To continue, enter - 0. To exit - any other character")
    code_wd = int(input())
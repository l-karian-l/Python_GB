# 2.3
month = int(input("Enter the number of month >>>"))

if month <= 0 or month > 12:

    print("There is no month with this number. Sry :(")

else:

    # 1 method

    mount_dir = {1: "winter", 2: "winter", 12: "winter",
                 3: "spring", 4: "spring", 5: "spring",
                 6: "summer", 7: "summer", 8: "summer",
                 9: "autumn", 10: "autumn", 11: "autumn"}
    print(mount_dir.get(month))

    # 2 method

    list1 = ["winter", "winter", "spring",
             "spring", "spring", "summer",
             "summer", "summer", "autumn",
             "autumn", "autumn", "winter"]

    print(list1[month-1])

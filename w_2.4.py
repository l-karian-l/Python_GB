# 2.4

words = input("Enter the text >>> ").split()

for i in words:

    if len(i) > 10:
        word1 = i[0:10]
        print(word1)
        continue
    else:
        print(i)
        

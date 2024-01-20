test_number = int(input())


for i in range(test_number):
    school_number = int(input())
    school_drinks = list()
    for j in range(school_number):
        name, drink = input().split()
        drink = int(drink)
        school_drinks.append([name,drink])

    school_drinks.sort(key=(lambda x: -x[1]))
    print (school_drinks[0][0])

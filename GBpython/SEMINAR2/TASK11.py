try:    
    number = int(input("Enter number: "))
    first = 0
    second = 1
    count = 2
    while second <= number:
        if second == number:
            print(count)
            break
        first, second = second, first + second
        count += 1
    else:
        print("-1")
except:
    print("Error!")
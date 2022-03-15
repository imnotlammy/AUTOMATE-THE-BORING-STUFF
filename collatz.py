print("Enter number:")
try:
    number = int(input())
    while True:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

except:
    print("Please enter an integer")

try:

    number = int(input('Enter a number: '))

    while number != 1:
        if (number % 2 == 0):
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

except ValueError:
    print('This script only accepts an integer!')
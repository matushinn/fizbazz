def fizzbazz_decide(number):
    if number % 15 == 0:
        print("fizzbazz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(str(number))


for number in range(1,101):
    fizzbazz_decide(number)


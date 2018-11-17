def fizzbuzz_convert(number):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(str(number))

for number in range(1,101):
        fizzbuzz_convert(number)







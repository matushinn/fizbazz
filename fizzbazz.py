def fizzbuzz_convert(number):
    if number % 15 == 0:
       return "fizzbuzz"
    elif number % 5 == 0:
       return "Buzz"
    elif number % 3 == 0:
       return "Fizz"
    else:
        return str(number)

for number in range(1,101):
        fizzbuzz_convert(number)







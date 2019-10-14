def fizzbuzz(a, b):
    for i in range(a, b+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

if __name__ == '__main__':
    start = int(input("Please input a start value: "))
    end = int(input("Please input an end value: "))
    fizzbuzz(start, end)

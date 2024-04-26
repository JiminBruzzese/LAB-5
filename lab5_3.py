def reverse_integer(number):
    reversed_num = 0
    while number != 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

def main():
    try:
        number = int(input("Enter a number: "))
        reversed_number = reverse_integer(abs(number))
        if number < 0:
            reversed_number *= -1  # Preserve the sign if the input number was negative
        print("Reversed number:", reversed_number)
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()

def count():
    numbers = input("Enter your list of numbers separated by spaces: ")
    number_list = numbers.split()  # Split the input string into individual numbers
    return len(number_list)

result = count()
print("Number of numbers entered:", result)

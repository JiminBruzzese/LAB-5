def volume(length, width, height):
    return length * width * height

while True:
    try: 
        length_input = input("What is the length of the box (or press 'quit' to exit): ")
        if length_input.lower() == "quit":
            break
        length = float(length_input)
        width = float(input("What is the width of the box: "))
        height = float(input("What is the height of the box: "))
    except ValueError:
        print("There was an error in your input, please try again.")
    
    print(volume(length,width,height))

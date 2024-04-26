def calculate_sum(N):
    return sum(range(1, N + 1))

def main():
    while True:
        try:
            user_input = input("Enter an integer (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            N = int(user_input)
            if N < 1:
                raise ValueError("Please enter a positive integer.")
            result = calculate_sum(N)
            print(f"Sum of integers from 1 to {N}: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

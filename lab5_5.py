def babylonian_sqrt(N, tolerance=1e-7, max_iterations=100):
    
    x = N / 2.0
   for _ in range(max_iterations):
        next_x = 0.5 * (x + N / x)
        if abs(x - next_x) < tolerance:
            return next_x
        x = next_x
def main():
    try:
        N = float(input("Enter a number to find its square root: "))
        if N < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        result = babylonian_sqrt(N)
        print(f"Square root of {N}: {result:.6f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

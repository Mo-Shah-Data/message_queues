from concurrent.futures import ProcessPoolExecutor

# Sample data
numbers = [1, 2, 3, 4, 5]


# Function to calculate the square of a number
def square(number):
    return number ** 2


def main():
    # Use ProcessPoolExecutor for parallel processing
    with ProcessPoolExecutor() as executor:
        # Map the function to the data in parallel
        results = list(executor.map(square, numbers))

    # Print the results
    print("Input numbers:", numbers)
    print("Squared numbers:", results)


if __name__ == "__main__":
    main()

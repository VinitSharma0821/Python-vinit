def main():
    data = []

    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program")
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == '1':
            data = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
            print("Data has been stored successfully!")

        elif choice == '2':
            if data:
                print("\nData Summary:")
                print(f"- Total elements: {len(data)}")
                print(f"- Minimum value: {min(data)}")
                print(f"- Maximum value: {max(data)}")
                print(f"- Sum of all values: {sum(data)}")
            else:
                print("No data found. Please input data first.")

        elif choice == '3':
            num = int(input("Enter a number to calculate factorial: "))

            def factorial(n):
                if n == 0 or n == 1:
                    return 1
                return n * factorial(n - 1)

            print(f"Factorial of {num} is {factorial(num)}")

        elif choice == '4':
            if data:
                threshold = int(input("Enter threshold value: "))
                filtered = list(filter(lambda x: x > threshold, data))
                print(f"Data after filtering (values > {threshold}): {filtered}")
            else:
                print("No data found. Please input data first.")

        elif choice == '5':
            if data:
                sorted_data = sorted(data)
                print(f"Sorted Data: {sorted_data}")
            else:
                print("No data found. Please input data first.")

        elif choice == '6':
            if data:
                def dataset_statistics(arr):
                    return min(arr), max(arr), sum(arr), len(arr)

                minimum, maximum, total_sum, count = dataset_statistics(data)
                print("\nDataset Statistics:")
                print(f"- Minimum: {minimum}")
                print(f"- Maximum: {maximum}")
                print(f"- Sum: {total_sum}")
                print(f"- Count: {count}")
            else:
                print("No data found. Please input data first.")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
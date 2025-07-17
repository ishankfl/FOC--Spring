def print_pattern(rows):
    for i in range(rows):
        # Print spaces for pyramid alignment
        print("   " * (rows - i - 1), end="")

        # # Increasing part: 2^0 to 2^i
        # for j in range(i + 1):
        #     print(f"{2**j:<3}", end="")

        # # Decreasing part: 2^(i-1) to 2^0
        for j in range(i - 1, -1, -1):
            print(f"{2**j:<3}", end="")

        print()  # Newline after each row

# Example usage
print_pattern(4)

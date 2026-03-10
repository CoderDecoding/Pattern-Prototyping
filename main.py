def print_pyramid(rows):
    print(f"\nGenerating a Pyramid with {rows} rows...")
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    print("\nLogic: Inner loop handles spaces (rows-i-1) and stars (2*i+1).")

rows = int(input("Enter number of rows: "))
print_pyramid(rows)
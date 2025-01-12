def main():
    while True:
        print("\nEnter 3 integers which are sides of a triangle:")
        try:
            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        print(f"\na={a}\tb={b}\tc={c}")

        # Check if values are in the permitted range
        c1 = 1 <= a <= 10
        c2 = 1 <= b <= 10
        c3 = 1 <= c <= 10

        if not c1:
            print(f"\nThe value of a={a} is not in the range of permitted values (1-10).")
        if not c2:
            print(f"\nThe value of b={b} is not in the range of permitted values (1-10).")
        if not c3:
            print(f"\nThe value of c={c} is not in the range of permitted values (1-10).")

        if c1 and c2 and c3:
            break

    # Check if the sides form a triangle
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Equilateral triangle")
        elif a != b and a != c and b != c:
            print("Scalene triangle")
        else:
            print("Isosceles triangle")
    else:
        print("Not a triangle")

if __name__ == "__main__":
    main()

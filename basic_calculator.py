from sys import exit


def main():
    while True:
        operation = input("Options: [Add] [Subtract] [Multiply] [Divide] or [Exit]\n")
        options = ("add", "subtract", "multiply", "divide", "exit")
        for i in options:
            if operation.lower() != i:
                continue
            elif operation.lower() == "exit":
                print("Shutting down...")
                exit(0)
            else:
                num_one = float(input("Enter the first number: "))
                num_two = float(input("Enter the first number: "))
                if operation.lower() == "add":
                    print(num_one + num_two)
                elif operation.lower() == "subtract":
                    print(num_one - num_two)
                elif operation.lower() == "multiply":
                    print(num_one * num_two)
                elif operation.lower() == "divide":
                    print(num_one / num_two)


if __name__ == '__main__':
    main()

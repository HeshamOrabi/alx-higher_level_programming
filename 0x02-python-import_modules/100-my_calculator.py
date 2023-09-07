#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1, sys

    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print(f"Enter int instade of {sys.argv[1]} or {sys.argv[3]}")
        sys.exit(1)

    if sys.argv[2] == '+':
        res = calculator_1.add(a, b)
    
    if sys.argv[2] == '-':
        res = calculator_1.sub(a, b)
    
    if sys.argv[2] == '*':
        res = calculator_1.mul(a, b)
    
    if sys.argv[2] == '/':
        res = calculator_1.div(a, b)

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))

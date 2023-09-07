#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    import sys

    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": calculator_1.add, "-": calculator_1.sub, "*": calculator_1.mul, "/": calculator_1.div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print(f"Enter int instade of {sys.argv[1]} or {sys.argv[3]}")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))

#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0

    for arg in sys.argv[1:]:

        try:
            sum += int(arg)
        except ValueError:
            print(f"Warning: Skipping invalid argument '{arg}'")
            
    print(sum)

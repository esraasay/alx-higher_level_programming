#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0

    for i in range(1, len(sys.argv)):
        try:
            total_sum += int(sys.argv[i])
        except ValueError:
            print("Error: Argument {} is not a valid integer".format(i))

    print(total_sum)

#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except (ValueError, TypeError):
        print("Error: Invalid input types")
        return None
    else:
        print("Inside result: {:.1f}".format(result))
        return result
    finally:
        print("Inside finally")

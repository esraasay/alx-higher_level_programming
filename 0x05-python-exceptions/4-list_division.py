def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(value_1, (int, float)) or \
               not isinstance(value_2, (int, float)):
                raise TypeError("wrong type")

            result = value_1 / value_2 if value_2 != 0 else 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except TypeError as e:
            print(e)
            result = 0
        finally:
            result_list.append(result)

    return result_list

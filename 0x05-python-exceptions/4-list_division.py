#!/usr/bin/python3



def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    for a in range(list_length):
        try:
            new_list[a] = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print('division by 0')
        except (ValueError, TypeError):
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            pass
    return new_list

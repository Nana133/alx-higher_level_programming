#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end='')
            no += 1
        except (ValueError, TypeError):
            x += 1
    print('')
    return no

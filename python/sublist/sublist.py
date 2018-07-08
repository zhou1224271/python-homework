SUBLIST = 1
SUPERLIST =2
EQUAL = 3
UNEQUAL = 4


def check_lists(first_list, second_list):
    len_first_str = len(first_list)
    len_second_str = len(second_list)

    if len_first_str == 0 and len_second_str != 0:
        return SUBLIST
    elif len_first_str != 0 and len_second_str == 0:
        return SUPERLIST
    elif len_first_str ==0 and len_second_str == 0:
        return EQUAL
    else:
        if first_list == second_list:
            return EQUAL
        else:
            if len_first_str > len_second_str:
                a_lst = [first_list[x:x+len_second_str] for x in range(0, len_first_str - len_second_str + 1)]
                for x in a_lst:
                    if second_list == x:
                        return SUPERLIST
                    else:
                        pass
                return UNEQUAL
            if len_first_str < len_second_str:
                b_lst = [second_list[x:x+len_first_str] for x in range(0, len_second_str - len_first_str + 1)]
                for x in b_lst:
                    if first_list == x:
                        return SUBLIST
                    else:
                        pass
                return UNEQUAL
            else:
                return UNEQUAL



def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    first_str_list = []
    sec_str_list = []
    for i in first_string:
        first_str_list.append(i)
    for i in second_string:
        sec_str_list.append(i)
    first_str_list.sort()
    sec_str_list.sort()
    return first_str_list == sec_str_list


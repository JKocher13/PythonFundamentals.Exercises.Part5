def is_palindrome(value) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    x = value.replace(" ","")
    y = x.lower()
    return y == y[::-1]


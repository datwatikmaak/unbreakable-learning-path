import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    result = []
    for char in input_string:
        if char in string.punctuation:
            result.append("")
        else:
            result.append(char)

    return "".join(result)

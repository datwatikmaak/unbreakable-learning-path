import string
from typing import List

ALPHANUMERIC = list(string.ascii_letters) + list(range(10))
print(ALPHANUMERIC)


def get_index_different_char(chars: List) -> int:
    alpha_num = []
    non_alpha_num = []
    for i, char in enumerate(chars):
        if char in ALPHANUMERIC:
            alpha_num.append(i)
        else:
            non_alpha_num.append(i)

    return alpha_num[0] if len(alpha_num) == 1 else non_alpha_num[0]


get_index_different_char(["A", "f", ".", "Q", 2])  # 2

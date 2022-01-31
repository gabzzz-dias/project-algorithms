def revert(word, low_index, high_index):
    if len(word) == 1:
        return word

    else:
        return revert(
            word[high_index], low_index, high_index
        ) + revert(word[:-1], low_index, high_index - 1)


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    reverted = revert(word, low_index, high_index)

    if reverted == word:
        return True
    else:
        return False

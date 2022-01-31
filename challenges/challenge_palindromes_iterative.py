def is_palindrome_iterative(word):
    if not word or word[0] != word[-1]:
        return False
    if len(word) == 1 or len(word) == 2 and word[0] == word[1]:
        return True

    return word == word[::-1]

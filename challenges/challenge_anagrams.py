def sorting(string):
    arr = list(string)
    result = []

    while arr:
        first = arr[0]

        for x in arr:
            if x < first:
                first = x

        result.append(first)
        arr.remove(first)

    return result


def is_anagram(first_string, second_string):
    return sorting(first_string) == sorting(second_string)

# Obtive ajuda do meu colega Ivan Rafael nos requisitos 3-5
# Valeu, Ivan!
# PR Ivan: https://github.com/tryber/sd-010-b-project-algorithms/pull/78

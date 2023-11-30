def quick_sort(s):
    if len(s) <= 1:
        return s

    pivot = s[0]
    less = []
    greater = []

    for i in range(1, len(s)):
        if s[i] <= pivot:
            less.append(s[i])
        else:
            greater.append(s[i])

    return quick_sort(less) + [pivot] + quick_sort(greater)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (
            "".join(quick_sort(first_string)),
            "".join(quick_sort(second_string)),
            False,
        )
    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first = quick_sort(first_string)
    sorted_second = quick_sort(second_string)
    are_anagrams = sorted_first == sorted_second

    return (
        "".join(sorted_first),
        "".join(sorted_second),
        are_anagrams,
    )

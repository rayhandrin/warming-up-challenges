def longest_substring(sample: str) -> int:
    substring_without_repeat = []

    for char in sample:
        if char not in substring_without_repeat:
            substring_without_repeat.append(char)
        else:
            substring_without_repeat.clear()

    return len("".join(substring_without_repeat))


print(longest_substring("abcabcbbklmnopq"))

def word_break(sample_string: str, dictionary: list) -> str:
    space_inserted = 0
    result = list(sample_string)

    for word in dictionary:
        indexes_to_insert = find_substring(sample_string, word)
        for index in indexes_to_insert:
            result.insert(
                indexes_to_insert.get(index) + len(word) + space_inserted, " "
            )
            space_inserted += 1

    return "".join(result).strip()


def find_substring(sample_string: str, substring: str) -> dict:
    correct_characters = 0
    substring_found = 1
    index_locator = {}

    for index, char in enumerate(sample_string):
        if char != list(substring)[correct_characters]:
            correct_characters = 0

        correct_characters += 1

        if correct_characters == len(substring):
            correct_characters = 0
            index_locator[substring_found] = index - (len(substring) - 1)
            substring_found += 1

    return index_locator


print(word_break("leetcode", ["leet", "code"]))

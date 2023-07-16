def check_similarites(sample: str, list_of_words: list) -> bool:
    for char in sample:
        if char in list_of_words[0]:
            if sample.count(char) != list_of_words[0].count(char):
                return False
        else:
            return False

    return True


def group_anagrams(sample_strings_in_list: list) -> list:
    grouped_anagrams = []
    is_member = None

    for word in sample_strings_in_list:
        if len(grouped_anagrams) == 0:
            grouped_anagrams.append([word])
        else:
            for words in grouped_anagrams:
                if check_similarites(word, words):
                    words.append(word)
                    is_member = True
                    break
                else:
                    is_member = False

            if is_member is False:
                grouped_anagrams.append([word])
                # is_member = True

    return grouped_anagrams


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

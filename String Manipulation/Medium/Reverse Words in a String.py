def reverse_words(sample_string: str) -> str:
    sample_string = sample_string.split()
    sample_string.reverse()

    return " ".join(sample_string)


print(reverse_words("the sky is blue"))

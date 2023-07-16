def move_zeroes(sample_list: list) -> str:
    zero_count = sample_list.count(0)
    sample_list = [elm for elm in sample_list if elm != 0]

    for n in range(zero_count):
        sample_list.append(0)

    return f"All zeroes have been moved: {sample_list}"


print(move_zeroes([1, 0, 0, 0, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0]))

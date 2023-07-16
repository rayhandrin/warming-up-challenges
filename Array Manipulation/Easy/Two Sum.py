def two_sum(sample_list: list, target: int) -> any:
    curr_idx = 0
    exiled_pair = set({})

    while curr_idx < (len(sample_list) - 1):
        for number in [num for num in sample_list if num != sample_list[curr_idx]]:
            if tuple(sorted([sample_list[curr_idx], number])) not in exiled_pair:
                if (sample_list[curr_idx] + number) == target:
                    return f"Target value found at indexes {[curr_idx, sample_list.index(number)]}"
                else:
                    exiled_pair.add(tuple(sorted([sample_list[curr_idx], number])))
        curr_idx += 1

    return "There's no correct pair of numbers for the target in the list."


print(two_sum([1, 2, 3, 4, 5, 6], 10))

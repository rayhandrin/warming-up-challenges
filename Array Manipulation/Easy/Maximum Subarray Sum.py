def max_subarr_sum(sample_list: list) -> str:
    curr_idx = 0
    temp_list = []
    biggest_sum = 0
    biggest_sublist = []

    while curr_idx < len(sample_list):
        temp_list.clear()
        temp_list.append(sample_list[curr_idx])
        for number in sample_list[(curr_idx + 1) :]:
            temp_list.append(number)
            if sum(temp_list) > biggest_sum:
                biggest_sum = sum(temp_list)
                biggest_sublist = temp_list.copy()
        curr_idx += 1

    return f"Biggest sum: {biggest_sum}, Sublist: {biggest_sublist}"


print(max_subarr_sum([1, -1, 4, 1, 2, 3, -1, 0, -5, 1]))

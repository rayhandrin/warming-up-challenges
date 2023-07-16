def merge_sorted_array(*sample_list: list) -> str:
    result_list = []

    for list in sample_list:
        result_list.extend(list)

    result_list.sort()

    return f"Successfully merged {len(sample_list)} list(s) into {result_list}"


print(merge_sorted_array([3, 4, 5], [1, 9, 2]))

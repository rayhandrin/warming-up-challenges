def remove_element(sample_list: list, element_to_be_removed: int) -> str:
    element_found = sample_list.count(element_to_be_removed)

    for idx in range(element_found):
        sample_list.remove(element_to_be_removed)

    return f"{element_to_be_removed} has been removed. Result: {sample_list}"


print(remove_element([3, 2, 2, 3, 1, 3, 5, 3, 2, 6, 5, 5, 7, 9, 9, 3], 3))

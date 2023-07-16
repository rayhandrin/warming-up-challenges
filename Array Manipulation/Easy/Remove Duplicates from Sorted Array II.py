def remove_duplicates_2(sample_list: list, element_to_be_removed: int) -> str:
    if sample_list.count(element_to_be_removed) <= 2:
        return "You can only remove element that has duplicates more than 2!"

    sample_list.remove(element_to_be_removed)

    return f"New list length: {len(sample_list)} / {sample_list}"


print(remove_duplicates_2([1, 2, 2, 2, 3, 4], 1))  # Succeed
print(remove_duplicates_2([1, 2, 2, 2, 3, 4], 1))  # Failed

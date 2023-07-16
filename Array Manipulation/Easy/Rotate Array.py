def rotate_array(sample_list: list, k: int, n_index: int) -> str:
    if k > (len(sample_list) - n_index):
        return "The amount of rotation you set is way too high!"

    for idx in range(k):
        sample_list.insert(idx, sample_list[n_index + idx])
        sample_list.pop(n_index + idx + 1)
    return f"Rotated array: {sample_list}"


print(rotate_array(["a", "b", "c", "d", "e"], 3, 1))

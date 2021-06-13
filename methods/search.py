from typing import List, Union


def binary_search(arr: List[int], find: int) -> Union[int, False]:
    def get_index(new_arr: List[int], depth: int) -> Union[int, False]:
        if len(new_arr) == 1 and new_arr[0] != find:
            return False

        piviot = new_arr[len(new_arr) // 2]
        if find < piviot:
            return get_index(new_arr[: len(new_arr) // 2], depth)
        elif find > piviot:
            return get_index(new_arr[len(new_arr) // 2 :], depth + len(new_arr) // 2)
        else:
            return len(new_arr) // 2 + depth

    return get_index(arr, 0)

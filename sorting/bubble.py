

def sort(arr_list: list):
    n = len(arr_list)
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
                swapped = True
        if not swapped:
            break
    return arr_list


def sort_recursive(arr_list: list, n: int):
    if n == 1:
        return arr_list
    swapped = False
    for i in range(n-1):
        if arr_list[i] > arr_list[i+1]:
            arr_list[i], arr_list[i+1] = arr_list[i+1], arr_list[i]
            swapped = True
    if not swapped:
        return arr_list
    return sort_recursive(arr_list, n-1)


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(sort(arr))
    print("----------------")
    print(sort_recursive(arr, len(arr)))
    # Output: [11, 12, 22, 25, 64]

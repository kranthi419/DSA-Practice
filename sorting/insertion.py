
def sort(arr_list):
    n = len(arr_list)
    for i in range(1, n):
        j = i
        while j > 0 and arr_list[j-1] > arr_list[j]:
            arr_list[j-1], arr_list[j] = arr_list[j], arr_list[j-1]
            j -= 1
    return arr_list


def sort_recursive(arr_list, i, n):
    if i == n:
        return arr_list
    j = i
    while j > 0 and arr_list[j-1] > arr_list[j]:
        arr_list[j-1], arr_list[j] = arr_list[j], arr_list[j-1]
        j -= 1
    return sort_recursive(arr_list, i+1, n)


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(sort(arr))
    print("----------------")
    print(sort_recursive(arr, 1, len(arr)))
    # Output: [11, 12, 22, 25, 64]

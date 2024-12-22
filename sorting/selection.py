

def sort(arr_list: list):
    n = len(arr_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr_list[j] < arr_list[min_idx]:
                min_idx = j
        arr_list[i], arr_list[min_idx] = arr_list[min_idx], arr_list[i]
    return arr_list


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(sort(arr))
    # Output: [11, 12, 22, 25, 64]

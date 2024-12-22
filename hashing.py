

def find_highest_lowest_frequency(arr: list):
    freq = {}
    for val in arr:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1
    max_freq = 0
    min_freq = len(arr)
    max_entry = None
    min_entry = None
    for key, val in freq.items():
        if val > max_freq:
            max_freq = val
            max_entry = key
        if val < min_freq:
            min_freq = val
            min_entry = key
    return max_entry, min_entry


def main():
    arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 0, 5]
    max_entry, min_entry = find_highest_lowest_frequency(arr)
    print(f"Max entry: {max_entry}, Min entry: {min_entry}")


if __name__ == "__main__":
    main()




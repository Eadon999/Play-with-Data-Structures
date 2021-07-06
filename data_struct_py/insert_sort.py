def insert_sort(src_arr):
    """升序从后往前扫描，对比大小，小则插入前边"""
    for i in range(1, len(src_arr)):
        for j in range(i, 0, -1):
            if src_arr[j] < src_arr[j - 1]:
                _temp = src_arr[j-1]
                src_arr[j-1] = src_arr[j]
                src_arr[j] = _temp
    print(src_arr)


if __name__ == '__main__':
    init_arr = [1, 5, 3, 3, 10, 9, 8, 11, 12]
    insert_sort(init_arr)

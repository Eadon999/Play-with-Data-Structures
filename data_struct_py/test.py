def quick_sort_self(alist, start, end):
    if start >= end:
        return

    mid = alist[start]

    low = start
    high = end

    while low < high:
        #
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1

        alist[high] = alist[low]

    alist[low] = mid

    print(low, high)

    # 对基准元素左边的子序列进行快速排序
    quick_sort_self(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort_self(alist, low + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("src:{}".format(alist))
    quick_sort_self(alist, 0, len(alist) - 1)
    print("sorted:{}".format(alist))

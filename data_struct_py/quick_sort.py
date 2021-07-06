def quick_sort(alist, start, end):
    """
    位置标识i，与j，i增，j减
    i=0选为基，右往左选小于基的index为j交换到i，再从左往右选出大于基的交换到当前j
    i+=1
    重复上述
    知道i>=j跳出循环
    再分别对两边进行quick sort
    """
    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    print("start low:{},high:{}".format(low, high))
    while low < high:
        # 从右往左找小于mid：如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            print("first low:{},high:{}".format(low, high))
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 从左往右找大于mid: 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            print("second low:{},high:{}".format(low, high))
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    print(low, high)

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("src:{}".format(alist))
    quick_sort(alist, 0, len(alist) - 1)
    print("sorted:{}".format(alist))

    # [17, 20, 26, 31, 44, 54, 55, 77, 93]

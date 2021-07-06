class MinHeap:
    def __init__(self, data):
        self.data = data
        self.create_min_heap()

    def left_child_index(self, idx):
        return idx * 2 + 1

    def right_child_index(self, idx):
        return idx * 2 + 2

    def parent_index(self, idx):
        return (idx - 1) // 2

    def create_min_heap(self):
        if len(self.data) == 0:
            print("arr just one element")
            return
        last_root_rode = self.parent_index(len(self.data) - 1)
        print("最后一个非叶节点：{}".format(last_root_rode))
        # for idx in range(last_root_rode, 0, -1):
        #     self.sift_down(idx)
        while last_root_rode >= 0:
            self.sift_down(last_root_rode)
            last_root_rode = last_root_rode - 1

    def sift_down(self, k):
        while self.left_child_index(k) < len(self.data):
            j = self.left_child_index(k)
            print("非叶节点：{}，左孩子节点：{}".format(k, j))
            if j + 1 < len(self.data) and self.data[j + 1] < self.data[j]:
                j = self.right_child_index(k)
                print("右孩子小于左孩子, j update as {}".format(j))

            print("k:{},j:{}, k_v:{},j_v:{}".format(k, j, self.data[k], self.data[j]))
            if self.data[k] <= self.data[j]:
                break

            print("k:{},j:{}".format(k, j))
            self.swap(k, j)
            k = j

    def swap(self, idx, another_idx):
        temp = self.data[idx]
        print("temp:{},k value:{}, j value:{}".format(temp, self.data[idx], self.data[another_idx]))
        self.data[idx] = self.data[another_idx]
        self.data[another_idx] = temp
        print("after temp:{},k value:{}, j value:{}".format(temp, self.data[idx], self.data[another_idx]))

    def find_min(self):
        if len(self.data) == 0:
            raise IndexError("empty heap")
        return self.data[0]

    def extract_min(self):
        min = self.find_min()
        self.swap(0, len(self.data) - 1)
        self.data.pop(len(self.data) - 1)
        self.sift_down(0)
        return min

    def replace(self, src_value):
        min = self.find_min()
        if src_value < min:
            print("小于堆顶元素，保持不变")
            return
        self.data[0] = src_value
        self.sift_down(0)


if __name__ == '__main__':
    a = [4, 7, 2, 5, 6, 1, 10, 3, 8]
    min_heap = MinHeap(a)
    print(min_heap.data)
    min_heap.replace(0)
    print(min_heap.data)
    print("===============================================")
    extract_num = 5
    res = []
    while extract_num > 0:
        min = min_heap.extract_min()
        res.append(min)
        print(min)
        extract_num -= 1
    print(res)

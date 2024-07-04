import sys

"""
1.快速排序算法模板
测试用例：
5
3 1 2 4 5
"""


def quick_sort(nums: list, l: int, r: int) -> None:
    if (l >= r):
        return
    x = nums[l+r >> 1]
    i = l-1
    j = r+1
    while i < j:
        i += 1
        while nums[i] < x:
            i += 1
        j -= 1
        while nums[j] > x:
            j -= 1
        if i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    quick_sort(nums, l, j)
    quick_sort(nums, j+1, r)


"""
2.归并排序算法模板
测试用例：
5
3 1 2 4 5
"""


def merge_sort(nums: list, l: int, r: int) -> None:
    if l >= r:
        return
    mid = l+r >> 1
    merge_sort(nums, l, mid)
    merge_sort(nums, mid+1, r)
    temp = []
    i = l
    j = mid+1
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    temp += nums[i:mid+1]
    temp += nums[j:r+1]
    nums[l:r+1] = temp


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    # quick_sort(nums, 0, n-1)
    merge_sort(nums, 0, n-1)
    print(" ".join(list(map(str, nums))))

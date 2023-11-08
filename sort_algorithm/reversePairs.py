

def reversePairs(nums):
    if len(nums) < 2:
        return 0
    tmp = [0 for _ in range(len(nums))]
    main_func(nums, 0, len(nums)-1, tmp)


def main_func(nums, left, right, tmp):

    if left == right:
        return 0
    
    mid = (left + right) //2

    left_pairs = main_func(nums, left, mid, tmp)
    right_pairs = main_func(nums, mid+1, right, tmp)

    cross_pairs = mergeAndCount(nums, left, mid, right, tmp)

    return left_pairs + right_pairs + cross_pairs


def cross_pairs(nums,left, mid, right, tmp):
    i = left
    j = mid + 1
    count = 0
    tmp = nums[left:right+1]

    while i <= mid and j <= high:   #只要左右两边都有数
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            count += (mid-i+1)
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1 
    nums[low:high+1] = tmp
    return count

from typing import List

def search(nums: List[int], target: int) -> int:
        n=len(nums)
        left_index=0
        right_index=n-1
        mid_index = (left_index+right_index)//2
        while left_index<=right_index:
            mid_index=(left_index+right_index)//2
            if nums[mid_index]>target:
                right_index=mid_index-1
            if nums[mid_index]<target:
                left_index=mid_index+1
            if nums[mid_index]==target:
                return mid_index
                
        return -1

nums = [1,2,3,4,5,6,7,8,12,35]
target = int(45)
a = search(nums,target)
print(a)
def rotate(nums, k):
    n = len(nums)
    k = k % n 
    nums[:] = nums[-k:] + nums[:-k]

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate(nums1, k1)
    print(nums1)

    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(nums2, k2)
    print(nums2)
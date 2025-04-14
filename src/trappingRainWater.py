def trap(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water_trapped += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water_trapped += right_max - heights[right]

    return water_trapped

# Example 1
N1 = 6
arr1 = [3, 0, 0, 2, 0, 4]
output1 = trap(arr1)
print(f"Example 1 Output: {output1} (Expected: 10)")

# Example 2
N2 = 4
arr2 = [7, 4, 0, 9]
output2 = trap(arr2)
print(f"Example 2 Output: {output2} (Expected: 10)")

# Example 3
N3 = 3
arr3 = [6, 9, 9]
output3 = trap(arr3)
print(f"Example 3 Output: {output3} (Expected: 0)")
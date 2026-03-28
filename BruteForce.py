"""
Brute Force:
[2, 3, 1, 2, 4] and target 7, we check every possible subarray and calculate their sum to find the minimum subarray whose sum is greater than or equal to 7. We iterate over each subarray of all possible lengths:
time complexity O(n^2) – We calculate the sum for every subarray, resulting in quadratic time complexity.

Shrinking Window Example
Problem: Find smallest subarray with
sum >= target.
Dry Run (Minimum Subarray Length Problem):
Array:
[2, 3, 1, 2, 4]
Target:
7
Brute Force:
For the array
[2, 3, 1, 2, 4] and target 7, we check every possible subarray and calculate their sum to find the minimum subarray whose sum is greater than or equal to 7. We iterate over each subarray of all possible lengths:
Subarray
[2] → sum = 2
Subarray
[3] → sum = 3
Subarray
[1] → sum = 1
Subarray
[2] → sum = 2
Subarray
[3, 1] → sum = 4
Subarray
[1, 2] → sum = 3
Subarray
[2, 3] → sum = 5
Subarray
[3, 1] → sum = 4
Subarray
[1, 2, 4] → sum = 7 (valid subarray, length = 3)
Subarray
[2, 3, 1] → sum = 7 (valid subarray, length = 3)
Subarray
[2, 4] → sum = 6
Subarray
[4] → sum = 4
The smallest valid subarray whose sum is ≥ 7 is
[1, 2, 4] with a length of 3.
This results in
O(n ^ 2) time complexity, as we calculate the sum for every possible subarray. """

#code
def small_sub_array(array,target):
    arr_length = len(array)
    min_length = float('inf')
    for start in range(arr_length):
        sum_arr = 0
        for end in range(start,arr_length):
            sum_arr += array[end] 
            if sum_arr >= target:
                length = end - start + 1 
                # if value = arr[0] start = 0 , end = 0 , length = 0 - 0 + 1 = 1 
                 # if value = arr[1] start = 1 , end = 1 , length = 1 - 1 + 1 = 1 
                  # if value = arr[2:3] start = 2 , end = 3 , length = 3 - 2 + 1 = 2 
                min_length = min(min_length,length)
                break    
    if min_length == float('inf'):
        return 0
    else: 
        return min_length

array = [2, 3, 1, 2, 4]
target = 7
print(small_sub_array(array,target))






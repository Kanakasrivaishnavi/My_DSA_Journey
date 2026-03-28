#Problem: Find smallest subarray with sum >= target.
#Two pointer technique
#time complexity - O(n)
#Each element is processed at most twice, once when added to the window and once when removed, making the solution linear in time. 
#Space Complexity: O(1)
          #The solution only uses a fixed amount of extra space for variables like start, sum, and minLen, so the space complexity is constant.
#Efficiency: Efficient for problems involving finding subarrays with specific sums or lengths, as it avoids recomputing sums multiple times.
#Best For:   Problems where you need to find the minimum or maximum subarray length satisfying certain conditions (like
             sum >= target)

def min_sub_arr(arr,target):
    start = 0
    length_arr = len(arr)
    min_len = float('inf')
    current_sum = 0 
    for end in range(length_arr):
        current_sum += arr[end]
        while  current_sum >= target: # loop execute only if condition is satisfied 
                length = end - start + 1 
                min_len = min(min_len,length) #find min length
                current_sum -= arr[start] #subtract the value in the start index then current_sum sum value will get update and 
                                          #move to condition in while loop and it check if it is true then loop will get execute else end will update               
                start += 1  #increase start value (move to right)
                
    if min_len == float('inf'):
        return 0
    else :
        return min_len

arr = list(map(int,input().split())) 
target = int(input())
print(min_sub_arr(arr,target))

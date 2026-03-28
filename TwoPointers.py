#problems in Two pointer technique

#Problem: Find smallest subarray with sum >= target.
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
                length = end - start + 1  # elemnts present in array
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


#Container With Most Water
#Problem Statement
#You are given an array height[] where each element represents the height of a vertical line.

#Find two lines such that together with the x-axis they form a container that holds the maximum amount of water.

#Return the maximum water that can be stored.

def tank_max_area(height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left # distence between left and right
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
height = list(map(int,input().split()))
print(tank_max_area(height))

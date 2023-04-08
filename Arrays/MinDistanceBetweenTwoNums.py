class Solution:
    def minDist(self, arr, n, x, y):
        
        min_distance = float('inf')
        prev_index = -1
    
        # Iterate through the array
        for i in range(n):
            if arr[i] == x or arr[i] == y:
                # Check if previous index has a different element
                if prev_index != -1 and arr[prev_index] != arr[i]:
                    min_distance = min(min_distance, i - prev_index)
                prev_index = i
    
        # If no such distance is possible, return -1
        if min_distance == float('inf'):
            return -1
        else:
            return min_distance
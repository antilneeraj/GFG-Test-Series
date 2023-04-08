class Solution:
    def largestAndSecondLargest(self, sizeOfArray, arr):
        max1 = max2 = -1
    
        # Find the maximum element
        for i in range(sizeOfArray):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2 and arr[i] != max1:
                max2 = arr[i]
    
        return max1, max2
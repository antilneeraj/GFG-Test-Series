class Solution:
    def thirdLargest(self, a, n):
        if n < 3:
            return -1
        else:
            # Initialize three largest elements as negative infinity
            first_largest = second_largest = third_largest = float('-inf')
            # Iterate through the array
            for i in range(n):
                # Update first largest if current element is greater
                if a[i] > first_largest:
                    third_largest = second_largest
                    second_largest = first_largest
                    first_largest = a[i]
                # Update second largest if current element is greater
                elif a[i] > second_largest and a[i] < first_largest:
                    third_largest = second_largest
                    second_largest = a[i]
                # Update third largest if current element is greater
                elif a[i] > third_largest and a[i] < second_largest:
                    third_largest = a[i]
            return third_largest
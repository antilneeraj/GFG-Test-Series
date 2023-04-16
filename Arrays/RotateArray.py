class Solution:
    def rotateArr(self, A, D, N):
        for i in range(D):
            A.append(A[i])
        del A[:D]

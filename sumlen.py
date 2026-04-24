class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]

        result = []

        for l, r in queries:
            if l == 0:
                sub_sum = prefix[r]
            else:
                sub_sum = prefix[r] - prefix[l - 1]

            length = r - l + 1
            result.append(sub_sum // length)

        return result

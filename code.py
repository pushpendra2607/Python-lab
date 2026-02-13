class Solution:
    def subarraySum(self, arr, target):
      left=0
      current=0
      for i in range(len(arr)):
        current+=arr[i]
        while current>target and left<=i:
          current-=arr[left]
          left+=1
        if current==target:
          return [left+1,right+1]
      return [-1]

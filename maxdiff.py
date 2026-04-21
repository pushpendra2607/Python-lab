class Solution:
    def maxMinDiff(self, arr, k):
        # code here
        arr.sort()
        def place(mid):
            count=1
            l=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-l>=mid:
                    count+=1
                    l=arr[i]
                if count>=k:
                    return True
            return False
        low=0
        high=arr[-1]-arr[0]
        ans=0
        while low<=high:
            mid=(low+high)//2
            if place(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
                

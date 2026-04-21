def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        t=0
        for i in nums:
            if t<0:
                t=0
            t+=i
            res=max(res,t)
        return res

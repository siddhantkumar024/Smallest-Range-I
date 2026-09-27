class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        maxn=max(nums)
        minn=min(nums)
        diff=(maxn-minn)
        return max(0,diff-2*k)
        

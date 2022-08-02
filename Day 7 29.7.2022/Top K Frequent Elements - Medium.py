class Solution:

    # def __init__(self,nums,n):
    #     self.nums = nums
    #     self.n = n


    def topKFrequent(self,nums,k):
        dict1={}
        for i in nums:
            if dict1.get(i,None) is None:
                dict1[i]=1
            else:
                dict1[i]+=1
        res=[]

        dict1=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))

        for n in dict1:
            res.append(n)
            k-=1
            if k==0:
                return res

sol = Solution()

nums = [1,1,1,1,2,2,2,3,3]
k = 2

print(sol.topKFrequent(nums,k))
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        arr=[]
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            if nums2[i]>stack[-1]:
                while stack and nums2[i]>stack[-1]:
                    x=stack.pop()
                    dic[x]=nums2[i]
                stack.append(nums2[i])      
            else:
                stack.append(nums2[i])
                dic[nums2[i]]=-1
        if len(stack)!=0:
            s=len(stack)
            for i in range(s):
                dic[stack.pop()]= -1
        for i in range(len(nums1)):
            arr.append((dic[nums1[i]]))
        return arr   
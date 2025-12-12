class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        answer = nums1+nums2
        answer.sort()
        mid =  len(answer)
        if mid % 2==0:
            return (answer[mid//2]+answer[mid//2-1])/2.0
        else:
            return answer[int(mid//2)]
"""
I think the pattern they want us to recognize here is binary search on both arrays would work to find the 
"middle" element and then we can average it out to find the median

Update: ok so that didn't work, I dont have an O(log(n + M)) solution but I think if we try to combine it
into one BIG list and find hte median of that it should be chill

Update 2: After watching big neetcodes explanation I THINK I MAY have a better understanding of this 
but after watching this ill try implementing it whilst following along.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #neetcode please save us
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        #run binary search on the smaller of the arrays to find the partition point
        if len(B) < len(A):
            A, B = B, A
        
        #run binary search on the smalle rone
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B (subtract 2 because we're at the index of value not length of list?)
            #what did navi mean by this?

            #get the values to compare to see if parition is good or not
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')

            #now check if both our bounds -> Aleft, Bright and Bleft and Aright
            #partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                #even
                return (max(Bleft, Aleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1 #reduce size of left parittion from A
            else:
                l = i + 1




        
        
        

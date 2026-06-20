#include <vector>
#include <algorithm>
#include <climits> // Needed for INT_MIN and INT_MAX

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Fix 1: Ensure nums1 is always the smaller array safely
        if (nums1.size() > nums2.size()) {
            std::swap(nums1, nums2); 
        }

        std::vector<int>& a = nums1;
        std::vector<int>& b = nums2;

        int total = a.size() + b.size();
        int half = total / 2;

        // Fix 2 & 3: Set right bound to a.size() to handle partitions cleanly
        int l = 0;
        int r = a.size(); 

        while (l <= r) {
            // Treat `i` as the NUMBER of elements taken from A, rather than just an index.
            // This prevents the C++ negative integer division infinite loop.
            int i = l + (r - l) / 2; 
            int j = half - i; 

            // Get values safely based on how many elements we took
            int a_left  = (i > 0) ? a[i - 1] : INT_MIN;
            int a_right = (i < a.size()) ? a[i] : INT_MAX;

            int b_left  = (j > 0) ? b[j - 1] : INT_MIN;
            int b_right = (j < b.size()) ? b[j] : INT_MAX;

            // Check if partition is correct
            if (a_left <= b_right && b_left <= a_right) {
                // Odd total elements
                if (total % 2 == 1) {
                    return std::min(a_right, b_right);
                }
                // Even total elements
                return (std::max(a_left, b_left) + std::min(a_right, b_right)) / 2.0;
            }  
            else if (a_left > b_right) {
                r = i - 1; // Too many elements from A, move left
            } 
            else {
                l = i + 1; // Too few elements from A, move right
            }
        }
        return 0.0;
    }
};
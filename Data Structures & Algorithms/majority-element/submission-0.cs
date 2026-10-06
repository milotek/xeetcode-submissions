public class Solution {
    public int MajorityElement(int[] nums) {
        Array.Sort(nums);
	    int len = nums.Length;
	    return nums[len/2];
    }
}